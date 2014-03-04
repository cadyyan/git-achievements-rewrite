"""
Goldsmith
	Reviewed patches before committing with git diff --cached
"""

from GitAchievements.achievements import UsageLeveledAchievement

class GoldsmithAchievement(UsageLeveledAchievement):
	"""
	Goldsmith
		Reviewed patches before committing with git diff --cached
	"""

	name        = 'Goldsmith'
	description = 'Reviewed patches before committing with git diff --cached'
	cmd         = 'diff .*--cached'

