"""
Hunter
	Used git bisect to perform a binary search to find which change introduced a bug
"""

from GitAchievements.achievements import UsageLeveledAchievement

class HunterAchievement(UsageLeveledAchievement):
	"""
	Hunter
		Used git bisect to perform a binary search to find which change introduced a bug
	"""

	name        = 'Hunter'
	description = 'Used git bisect to perform a binary search to find which achievement introduced a bug'
	cmd         = 'bisect'

