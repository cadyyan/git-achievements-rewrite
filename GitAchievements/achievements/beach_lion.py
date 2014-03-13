"""
Beach Lion
	Restricted login shell for GIT-only SSH access with git-shell
"""

from GitAchievements.achievements import SingleUseAchievement

class BeachLionAchievement(SingleUseAchievement):
	"""
	Beach Lion
		Restricted login shell for GIT-only SSH access with git-shell
	"""

	name        = 'Beach Lion'
	description = 'Restricted login shell for GIT-only SSH access with git-shell'
	cmd         = 'shell'

