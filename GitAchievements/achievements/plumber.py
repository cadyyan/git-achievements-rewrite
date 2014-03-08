"""
Plumber
	Use the internal plumbing commands of git
"""

from GitAchievements.achievements import UsageLeveledAchievement

class PlumberAchievement(UsageLeveledAchievement):
	"""
	Plumber
		Use the internal plumbing commands of git
	"""

	name = 'Plumber'
	description = 'Use the internal plumbing commands of git'
	cmd         = r'(hash\-object|update\-index|commit\-tree|update\-ref)'

