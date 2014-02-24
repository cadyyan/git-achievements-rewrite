"""
File based storing of data.
"""

from GitAchievements.achievements.base import Achievement
from GitAchievements.store.base import Store
import GitAchievements.util

import datetime
import os
import re

class LogFileStore(Store):
	"""
	Similar to the traditional log file storing of data.
	"""

	ACHIEVEMENT_REGEX = re.compile(r'\*{80}\s+Git Achievement Unlocked\!\s+(.*)\s+.*\s+\*{80}')
	META_REGEX        = re.compile(r'((\w+ ?)+)(\((.*)\))?')

	def __init__(self, git_config):
		"""
		Setup the store to point to the git config log files.
		"""

		super(LogFileStore, self).__init__(git_config)

		self.log_file_path = self.config.get_value(
				'achievement', 'log_file',
				default = GitAchievements.util.expand_filepath('~/.git-achievements.log'))

		self.action_log_file_path = self.config.get_value(
				'achievement', 'action_log_file',
				default = GitAchievements.util.expand_filepath('~/.git-achievements-action.log'))

	def get_unlocked_achievements(self):
		achievements = Achievement.get_plugins()

		if os.path.exists(self.log_file_path):
			with open(self.log_file_path, 'r') as log_file:
				log = log_file.read()
		else:
			log = ''

		achievement_strings = [s.strip() for s in self.ACHIEVEMENT_REGEX.findall(log)]
		unlocked            = []
		for unlocked_str in achievement_strings:
			groups = self.META_REGEX.match(unlocked_str).groups()

			if len(groups) == 4 and groups[3]:
				name = re.sub(r'^(Apprentice|Master)', '', groups[0]).strip()
				meta = groups[3].strip()
			else:
				name = groups[0]
				meta = None

			for achiev in achievements:
				if achiev.name == name:
					achiev_instance = achiev.from_string(meta)
					unlocked.append(achiev_instance)

		return unlocked

	def unlock_achievement(self, achievement):
		log_record  = _format_line('*' * 80)
		log_record += _format_line('Git Achievement Unlocked!')
		log_record += _format_line('')
		log_record += _format_line(achievement.get_formatted_name())
		log_record += _format_line(achievement.description)
		log_record += _format_line('*' * 80)

		with open(self.log_file_path, 'a+') as log_file:
			log_file.write(log_record)

	def get_usage_count(self, command):
		if not os.path.exists(self.action_log_file_path):
			return 0

		with open(self.action_log_file_path, 'r') as action_file:
			actions = action_file.read()

		usage = re.findall(command, actions)
		return len(usage)

	def log_action(self, action):
		timestamp = datetime.datetime.utcnow()

		action_record  = '{0}\n'.format(action)
		action_record += 'Date: {0}\n'.format(timestamp.strftime('%a %b %d %H:%M:%S UTC %Y'))

		with open(self.action_log_file_path, 'a+') as action_file:
			action_file.write(action_record)

def _format_line(line):
	"""
	Format a line into a format thats suitable for a console/terminal.
	"""

	padding       = 80 - len(line)
	left_padding  = padding / 2
	right_padding = padding - left_padding

	line = ' ' * left_padding + line + ' ' * right_padding

	return line + '\n'

