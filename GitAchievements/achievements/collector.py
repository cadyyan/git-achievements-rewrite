"""
Collector
	Fetches named head or tags from another repository with git fetch
"""

from GitAchievements.achievements import UsageLeveledAchievement

class CollectorAchievement(UsageLeveledAchievement):
	"""
	Collector
		Fetches named head or tags from another repository with git fetch
	"""

	name        = 'Collector'
	description = 'Fetches named head or tags from another repository with git fetch'
	cmd         = 'fetch'

