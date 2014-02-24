"""
Chimney Sweeper
	Used git gc to run a number of housekeeping tasks on the current repository
"""

from GitAchievements.achievements import UsageLeveledAchievement

class ChimneySweeperAchievement(UsageLeveledAchievement):
	"""
	Chimney Sweeper
		Used git gc to run a number of housekeeping tasks on the current repository
	"""

	name        = 'Chimney Sweeper'
	description = 'Used git gc to run a number of housekeeping tasks on the current repository'
	cmd         = 'gc'

