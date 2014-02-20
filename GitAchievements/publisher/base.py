"""
Base publisher interface. A publisher writes out a summary of unlocked achievements.
"""

# pylint: disable=R0921

import GitAchievements.plugin

class Publisher(GitAchievements.plugin.Plugin):
	"""
	Base publisher interface. A publisher writes out a summary of unlocked achievements.
	"""

	def __init__(self, app):
		"""
		Setup the publisher.
		"""

		self.config = app.config

	def publish(self, app):
		"""
		Publish the given achievements. A list of files that should be added to the git repo
		should be returned.
		"""

		raise NotImplementedError('publish not implemented yet')

