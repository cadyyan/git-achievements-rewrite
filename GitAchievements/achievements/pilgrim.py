"""
Pilgrim
	Performed a rebase using git rebase --onto
"""

from GitAchievements.achievements import UsageLeveledAchievement

class PilgrimAchievement(UsageLeveledAchievement):
	"""
	Pilgrim
		Performed a rebase using git rebase --onto
	"""

	name        = 'Pilgrim'
	description = 'Performed a rebase using git rebase --onto'
	cmd         = 'rebase .*--onto'

