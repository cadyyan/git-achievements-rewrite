"""
Blacksmith
	Created a branch using git checkout -b
"""

from GitAchievements.achievements import UsageLeveledAchievement

class BlacksmithAchievement(UsageLeveledAchievement):
	"""
	Blacksmith
		Created a branch using git checkout -b
	"""

	name        = 'Blacksmith'
	description = 'Created a branch using git checkout -b'
	cmd         = r'checkout .*\-b'

