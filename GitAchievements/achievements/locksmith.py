"""
Locksmith
	Add Signed-off-by line at the end of the commit log message using git commit -s
"""

from GitAchievements.achievements import UsageLeveledAchievement

class LocksmithAchievement(UsageLeveledAchievement):
	"""
	Locksmith
		Add Signed-off-by line at the end of the commit log message using git commit -s
	"""

	name        = 'Locksmith'
	description = 'Add signed-off-by line at the end of the commit log message using git commit -s'
	cmd         = 'commit .*-s'

