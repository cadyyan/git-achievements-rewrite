"""
The base git achievement class.
"""

# pylint: disable=R0921,R0922

import GitAchievements.plugin

import math

class Achievement(GitAchievements.plugin.Plugin):
	"""
	The base git achievement class.
	"""

	can_level = True

	def __init__(self, level = None):
		"""
		Sets up the achievement object.

		level - the level unlocked (can be None)
		"""

		self.level = level

	def get_formatted_name(self):
		"""
		Gets a pretty formatted name for the achievement.
		"""

		if not self.level:
			prefix = ''
		elif self.level <= 3:
			prefix = 'Apprentice '
		elif self.level > 6:
			prefix = 'Master '
		else:
			prefix = ''

		postfix = ' (Level {0})'.format(self.level) if self.level else ''

		return '{0}{1}{2}'.format(prefix, self.name, postfix)

	def __eq__(self, other):
		"""
		Check if these two achievements have the same name.
		"""

		return self.name == other.name

	def __ne__(self, other):
		"""
		Check if these two achievmeents do not have the same name.
		"""

		return self.name != other.name

	@classmethod
	def check_condition(cls, app):
		"""
		Checks if the condition has been met for unlocking this achievement.
		"""

		raise NotImplementedError('check_condition not implemented yet')

class UsageLeveledAchievement(Achievement):
	"""
	Achievement that is leveled up through normal usage.
	"""

	name        = None
	description = None
	cmd         = None

	@classmethod
	def check_condition(cls, app):
		current_level = app.get_current_level(cls.name)
		required      = sum([math.pow(2, level) for level in range(1, current_level + 2)])
		usage         = app.store.get_usage_count(cls.cmd)

		if usage < required:
			return None

		return cls(level = current_level + 1)

