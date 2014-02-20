#!/usr/bin/env python

# pylint: disable=C0103,C0111

from GitAchievements.achievements import Achievement
from GitAchievements.plugin import Plugin, load_plugins
import GitAchievements.publisher
import GitAchievements.store
import GitAchievements.util

import argparse
import git
import git.config
import git.exc
import os.path
import sys

GIT_CMD = '/usr/bin/git'

class GitAchievementsApp(object):
	"""
	The achievements application.
	"""

	def __init__(self):
		"""
		Setup the application.
		"""

		self.config = git.config.GitConfigParser(GitAchievements.util.expand_filepath('~/.gitconfig'))

		self.achievements_dir = self._get_achievements_dir()
		external_plugin_dir = self.config.get_value(
				'achievement', 'plugin_dir',
				default = os.path.join(self.achievements_dir, 'plugins'))

		plugin_dirs = [
			external_plugin_dir,
		]

		load_plugins(plugin_dirs)

		store_type_name = self.config.get_value('achievement', 'store_type',
												default = 'GitAchievements.store.file.LogFileStore')
		store_type      = Plugin.get_plugin_by_name(store_type_name)
		if not store_type:
			print 'Invalid achievement store plugin selected:\n{0}'.format(store_type_name)
			sys.exit(1)

		self.store = store_type(self.config)

		self.all_achievements      = [ a for a in Achievement.get_plugins() if a.name ]
		self.unlocked_achievements = self.store.get_unlocked_achievements()
		self.locked_achievements   = [
			a for a in self.all_achievements if a not in self.unlocked_achievements or a.can_level
		]

		self.repo = None
		try:
			self.repo = git.Repo('.')
			self.git  = self.repo.git
		except git.exc.InvalidGitRepositoryError:
			self.git = git.Git()

	def run(self):
		"""
		Run the application.
		"""

		# Check if we're handling an achievements command. If not pass it on!
		command_args = sys.argv[1:]
		try:
			if len(command_args) > 0 and command_args[0] == 'achievements':
				self._handle_achievements_commands()
			else:
				self.git.execute([GIT_CMD] + command_args)
		except SystemExit:
			pass # Prevent exiting

		# Log the action
		self.store.log_action(' '.join(command_args))

		# Check if we unlocked anything
		for achievement in self.locked_achievements:
			achievements = achievement.check_condition(self)
			if not achievements:
				continue

			achievements = [achievements] if type(achievements) != list else achievements

			for achievement_inst in achievements:
				self._print_achievement(achievement_inst)
				self.store.unlock_achievement(achievement_inst)

	def get_current_level(self, achievement_name):
		"""
		Gets the current level for an achievement.
		"""

		achievement = [a for a in self.unlocked_achievements if a.name == achievement_name]
		achievement.sort(key = lambda a: a.level, reverse = True)

		if len(achievement) == 0:
			current_level = 0
		else:
			current_level = achievement[0].level

		return current_level

	def get_points(self):
		"""
		Gets the total number of points currently earned.
		"""

		points = 0
		for achievement in self.unlocked_achievements:
			if achievement.can_level:
				points += achievement.level

			points += 1

		return points

	def _handle_achievements_commands(self):
		"""
		Handles the achievement related commands.
		"""

		# pylint: disable=C0301
		cmd_parser = argparse.ArgumentParser(description = 'Git Achievements')
		group = cmd_parser.add_mutually_exclusive_group(required = True)
		group.add_argument('-p', '--publish',
				dest = 'publish', action = 'store_true',
				help = 'Generate achievements html files and if achievements.upload is set to \"true\" add the files and push to origin.')
		group.add_argument('-l', '--list',
				dest = 'list', action = 'store_true',
				help = 'Show all achievements.')
		# pylint: enable=C0301

		args = cmd_parser.parse_args(sys.argv[2:])

		if args.publish:
			self._handle_command_publish()
		elif args.list:
			self._handle_command_list()

	def _handle_command_publish(self):
		"""
		Handle the publish command.
		"""

		self._publish_achievements()

	def _handle_command_list(self):
		"""
		Handle the list command.
		"""

		if len(self.unlocked_achievements) == 0:
			print 'No achievements unlocked yet'
			return

		for achievement in self.unlocked_achievements:
			self._print_achievement(achievement)

	def _publish_achievements(self):
		"""
		Publish achievements.
		"""

		publishers = self.config.get_value(
			'achievement', 'publishers',
			default = 'GitAchievements.publisher.HtmlPublisher').split(';')
		publishers = [p for p in publishers if p != '']

		if len(publishers) == 0:
			print 'No publishers selected'
			return

		files = []
		for publisher in publishers:
			publisher = Plugin.get_plugin_by_name(publisher)(self)

			new_files = publisher.publish(self)
			if not new_files:
				new_files = []
			elif type(new_files) != list:
				new_files = [new_files]

			files += new_files

		if self.config.get_value(
			'achievement', 'upload',
			default = 'false').lower() == 'true':
			achievements_repo = git.Repo(self.achievements_dir)
			achievements_repo.index.add(files)
			achievements_repo.index.commit('Publish achievements')

			achievements_repo.remotes.origin.push()
		else:
			print 'Global achievement.upload not set to true, uploads left uncommited'

	@staticmethod
	def _print_achievement(achievement):
		"""
		Print achievement to console.
		"""

		print _format_line('*' * 80)
		print _format_line('Git Achievement Unlocked!')
		print _format_line('')
		print _format_line(achievement.get_formatted_name())
		print _format_line(achievement.description)
		print _format_line('*' * 80)

	@staticmethod
	def _get_achievements_dir():
		"""
		Get the git achievements directory.
		"""

		return os.path.dirname(sys.argv[0])

def _format_line(line):
	"""
	Format a line into a format thats suitable for a console/terminal.
	"""

	padding       = 80 - len(line)
	left_padding  = padding / 2
	right_padding = padding - left_padding

	line = ' ' * left_padding + line + ' ' * right_padding

	return line

if __name__ == '__main__':
	GitAchievementsApp().run()

