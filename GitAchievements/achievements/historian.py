"""
Historian
	Investigate the commit log using git log
"""

from GitAchievements.achievements import UsageLeveledAchievement

class HistorianAchievement(UsageLeveledAchievement):
	"""
	Historian
		Investigate the commit log using git log
	"""

	name        = 'Historian'
	description = 'Investigate the commit log using git log'
	cmd         = 'log'

