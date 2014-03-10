"""
Thug
	Forced pushed a branch with git push -f
"""

from GitAchievements.achievements import UsageLeveledAchievement

class ThugAchievement(UsageLeveledAchievement):
	"""
	Thug
		Forced pushed a branch with git push -f
	"""

	name        = 'Thug'
	description = 'Forced pushed a branch with git push -f'
	cmd         = r'push .*-(f|\-force)'

