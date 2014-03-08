"""
Merchant
	Added an external repository with git remote add
"""

from GitAchievements.achievements import UsageLeveledAchievement

class MerchantAchievement(UsageLeveledAchievement):
	"""
	Merchant
		Added an external repository with git remote add
	"""

	name        = 'Merchant'
	description = 'Added an external repository with git remote add'
	cmd         = 'remote add'

