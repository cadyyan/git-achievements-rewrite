"""
Architect
	Created a new repository with git-init.
"""

from GitAchievements.achievements.base import UsageLeveledAchievement

class ArchitectAchievement(UsageLeveledAchievement):
	"""
	Architect
		Created a new repository with git-init.
	"""

	name        = 'Architect'
	description = 'Created a new repository with git-init.'
	cmd         = 'init'

