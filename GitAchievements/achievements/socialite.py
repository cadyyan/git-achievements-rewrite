"""
Socialite
	Pushed a branch to a remote repository using git push
"""

from GitAchievements.achievements import UsageLeveledAchievement

class SocialiteAchievement(UsageLeveledAchievement):
	"""
	Socialite
		Pushed a branch to a remote repository using git push
	"""

	name        = 'Socialite'
	description = 'Pushed a branch to a remote repository using git push'
	cmd         = 'push' # TODO: there might be issues with dry runs

