"""
Homeowner
	Set global email address using git config
"""

from GitAchievements.achievements import SingleUseAchievement

class HomeownerAchievement(SingleUseAchievement):
	"""
	Homeowner
		Set global email address using git config
	"""

	name        = 'Homeowner'
	description = 'Set global email address using git config'
	cmd         = 'config --global user.email'

