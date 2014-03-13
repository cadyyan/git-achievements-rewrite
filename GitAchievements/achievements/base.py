"""
The base git achievement class.
"""

# pylint: disable=R0921,R0922

import GitAchievements.plugin

import math
import re

class Achievement(GitAchievements.plugin.Plugin):
	"""
	The base git achievement class.
	"""

	def __init__(self, *args, **kwargs):
		"""
		Create an achievement object
		"""

	def get_formatted_name(self):
		"""
		Gets a pretty formatted name for the achievement.
		"""

		return self.name

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
	def check_condition(cls, app, command_args):
		"""
		Checks if the condition has been met for unlocking this achievement.
		"""

		raise NotImplementedError('check_condition not implemented yet')

	@classmethod
	def from_string(cls, formatted_string):
		"""
		Creates an achievement object from the formatted string.
		"""

		return cls()

class LeveledAchievement(Achievement):
	"""
	An achievement that is leveled up in some way.
	"""

	name        = None
	description = None

	def __init__(self, level):
		"""
		Create an achievement at the given level.
		"""

		super(LeveledAchievement, self).__init__()

		self.level = level

	def get_formatted_name(self):
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
		Checks the achievement name and the level.
		"""

		if not isinstance(other, LeveledAchievement):
			return False

		return self.name == other.name and self.level == other.level

	def __ne__(self, other):
		"""
		Checks the achievement name and the level.
		"""

		return self.name != other.name or self.level != other.level

	@classmethod
	def from_string(cls, formatted_string):
		level = int(re.search(r'Level (\d+)', formatted_string).groups()[0])
		return cls(level)

class UsageLeveledAchievement(LeveledAchievement):
	"""
	Achievement that is leveled up through normal usage.
	"""

	name        = None
	description = None
	cmd         = None

	@classmethod
	def check_condition(cls, app, command_args):
		current_level = app.get_current_level(cls.name)
		required      = sum([math.pow(2, level) for level in range(1, current_level + 2)])
		usage         = app.store.get_usage_count(cls.cmd)

		if usage < required:
			return None

		return cls(level = current_level + 1)

class SingleUseAchievement(Achievement):
	"""
	An achievement that needs to be used once to be unlocked.
	"""

	name        = None
	description = None
	cmd         = None

	@classmethod
	def check_condition(cls, app, command_args):
		usage = app.store.get_usage_count(cls.cmd)
		if usage == 0:
			return None

		if len([a for a in app.unlocked_achievements if a.name == cls.name]) > 0:
			return None

		return cls()

