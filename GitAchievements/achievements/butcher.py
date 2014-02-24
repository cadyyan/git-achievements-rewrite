"""
Butcher
	Performed an interactive rebase using git rebase -i
"""

from GitAchievements.achievements import UsageLeveledAchievement

class ButcherAchievement(UsageLeveledAchievement):
	"""
	Butcher
		Performed an interactive rebase using git rebase -i
	"""

	name        = 'Butcher'
	description = 'Performed an interactive rebase using git rebase -i'
	cmd         = r'rebase .*\-i'

