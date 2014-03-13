"""
Inventor
	Used a command that isn't part of the built in Git command
"""

from GitAchievements.achievements.base import Achievement

import os.path
import sys

class InventorAchievement(Achievement):
	"""
	Inventor
		Used a command that isn't part of the built in Git command
	"""

	name        = 'Inventor'
	description = 'Used a command that isn\'t part of the built in Git command'

	def __init__(self, cmd):
		"""
		Create inventor achievement for specific command.
		"""

		super(InventorAchievement, self).__init__()

		self.cmd = cmd

	def get_formatted_name(self):
		return '{0} ({1})'.format(self.name, self.cmd)

	def __eq__(self, other):
		"""
		Checks the name and the command.
		"""

		return self.name == other.name and self.cmd == other.cmd

	def __ne__(self, other):
		"""
		Checks the name and the command.
		"""

		return self.name != other.name or self.cmd != other.cmd

	@classmethod
	def from_string(cls, formatted_string):
		return cls(formatted_string)

	@classmethod
	def check_condition(cls, app, command_args):
		git_core_path = app.git.execute([app.git_cmd, '--exec-path'])
		subcommand    = sys.argv[1]

		if subcommand.startswith('-'):
			return None

		git_ext = 'git-' + subcommand

		if os.path.exists(os.path.join(git_core_path, git_ext)):
			return None

		if subcommand == 'achievements':
			return None

		usage = app.store.get_usage_count(subcommand)
		if usage > 1: # TODO: it would be better to check if this achievement has been unlocked already
			return None

		return cls(subcommand)

