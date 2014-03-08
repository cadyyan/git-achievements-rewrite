"""
Stone Mason
	Added files to the index area for inclusion in the next commit with git add
"""

from GitAchievements.achievements import UsageLeveledAchievement

class StoneMasonAchievement(UsageLeveledAchievement):
	"""
	Socialite
		Pushed a branch to a remote repository using git push
	"""

	name        = 'Stone Mason'
	description = 'Pushed a branch to a remote repository using git push'
	cmd         = 'add'

