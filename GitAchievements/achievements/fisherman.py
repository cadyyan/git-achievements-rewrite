"""
Fisherman
	Look for specified patterns in the current repository with git grep
"""

from GitAchievements.achievements import UsageLeveledAchievement

class FishermanAchievement(UsageLeveledAchievement):
	"""
	Fisherman
		Look for specified patterns in the current repository with git grep
	"""

	name        = 'Fisherman'
	description = 'Look for specified patterns in the current repository with git grep'
	cmd         = 'grep'

