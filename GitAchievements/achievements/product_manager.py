"""
Product Manager
	Stash the changes in a dirty working directory away with git stash
"""

from GitAchievements.achievements import UsageLeveledAchievement

class ProductManagerAchievement(UsageLeveledAchievement):
	"""
	Product Manager
		Stash the changes in a dirty working directory away with git stash
	"""

	name        = 'Product Manager'
	description = 'Stash changes in a dirty working directory away with git stash'
	cmd         = 'stash'

