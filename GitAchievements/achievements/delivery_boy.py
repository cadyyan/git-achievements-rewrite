"""
Delivery Boy
	Move objects and refs by archive with git-bundle
"""

from GitAchievements.achievements import SingleUseAchievement

class DeliveryBoyAchievement(SingleUseAchievement):
	"""
	Delivery Boy
		Move objects and refs by archive with git-bundle
	"""

	name        = 'Delivery Boy'
	description = 'Move objects and refs by archive with git-bundle'
	cmd         = 'bundle'

