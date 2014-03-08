"""
Seamstress
	Amended a commit with git commit --amend
"""

from GitAchievements.achievements import UsageLeveledAchievement

class SeamstressAchievement(UsageLeveledAchievement):
	"""
	Seamstress
		Amended a commit with git commit --amend
	"""

	name        = 'Seamstress'
	description = 'Amended a commit with git commit --amend'
	cmd         = 'commit .*--amend'

