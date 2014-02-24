"""
Cleaning Lady
	Remove untracked files from the working tree with git clean
"""

from GitAchievements.achievements import UsageLeveledAchievement

class CleaningLadyAchievement(UsageLeveledAchievement):
	"""
	Cleaning Lady
		Remove untracked files from the working tree with git clean
	"""

	name        = 'Cleaning Lady'
	description = 'Remove untracked files from the working tree with git clean'
	cmd         = 'clean'

