"""
Weaver
	Investigate old branches by using git-reflog
"""

from GitAchievements.achievements import SingleUseAchievement

class WeaverAchievement(SingleUseAchievement):
	"""
	Weaver
		Investigate old branches by using git-reflog
	"""

	name        = 'Weaver'
	description = 'Investigate old branches by using git-reflog'
	cmd         = 'reflog'

