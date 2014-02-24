"""
Author
	Made 2^Level commits using git commit
"""

from GitAchievements.achievements import UsageLeveledAchievement

class AuthorAchievement(UsageLeveledAchievement):
	"""
	Author
		Made 2^Level commits using git commit
	"""

	name        = 'Author'
	description = 'Made 2^Level commits using git commit'
	cmd         = 'commit'

