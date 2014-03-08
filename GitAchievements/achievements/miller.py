"""
Miller
	Add only part of a file to the stage with git add -p
"""

from GitAchievements.achievements import UsageLeveledAchievement

class MillerAchievement(UsageLeveledAchievement):
	"""
	Miller
		Add only part of a file to the stage with git add -p
	"""

	name        = 'Miller'
	description = 'Add only part of a file to the stage with git add -p'
	cmd         = 'add .*-p'

