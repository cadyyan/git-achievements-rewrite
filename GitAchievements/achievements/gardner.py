"""
Gardner
	Shows the commit ancestry graph with git show-branch
"""

from GitAchievements.achievements import UsageLeveledAchievement

class GardnerAchievement(UsageLeveledAchievement):
	"""
	Gardner
		Shows the commit ancestry graph with git show-branch
	"""

	name        = 'Gardner'
	description = 'Shows the commit ancestry graph with git show-branch'
	cmd         = 'show-branch'

