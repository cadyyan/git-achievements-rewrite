"""
Data store for keeping track of achievements.
"""

# pylint: disable=R0921

import GitAchievements.plugin

class Store(GitAchievements.plugin.Plugin):
	"""
	Data store base implementation.
	"""

	def __init__(self, git_config):
		"""
		Sets up the data store based on the git config settings.
		"""

		self.config = git_config

	def get_unlocked_achievements(self):
		"""
		Get all the achievements that have been unlocked.
		"""

		raise NotImplementedError('get_unlocked_achievements not implemented yet')

	def unlock_achievement(self, achievement):
		"""
		Marks an achievement as unlocked.
		"""

		raise NotImplementedError('unlock_achievement not implemented yet')

	def get_usage_count(self, command):
		"""
		Gets the usage count for the given command.
		"""

		raise NotImplementedError('get_usage_count not implemented yet')

	def log_action(self, action):
		"""
		Logs an action for later review.
		"""

		raise NotImplementedError('log_action not implemented yet')

