"""
Archivist
	Prepare each commit with its patch in one file per commit with git format-patch
"""

from GitAchievements.achievements import UsageLeveledAchievement

class ArchivistAchievement(UsageLeveledAchievement):
	"""
	Archivist
		Prepare each commit with its patch in one file per commit with git format-patch
	"""

	name        = 'Archivist'
	description = 'Prepare each commit with its patch in one file per commit with git format-patch'
	cmd         = 'format-patch'

