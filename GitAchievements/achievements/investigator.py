"""
Investigator
	Used git blame to annotate a file with information about how each line changed
"""

from GitAchievements.achievements import UsageLeveledAchievement

class InventorAchievement(UsageLeveledAchievement):
	"""
	Investigator
		Used git blame to annotate a file with information about how each line changed
	"""

	name        = 'Investigator'
	description = 'Used git blame to annotate a file with information about how each line changed'
	cmd         = 'blame'

