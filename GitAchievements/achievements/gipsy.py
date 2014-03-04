"""
Gipsy
	Create, list, delete a tag signed with GPG using git tag
"""

from GitAchievements.achievements import UsageLeveledAchievement

class GipsyAchievement(UsageLeveledAchievement):
	"""
	Gipsy
		Create, list, delete a tag signed with GPG using git tag
	"""

	name        = 'Gipsy'
	description = 'Create, list, delete a tag signed with GPG using git tag'
	cmd         = 'tag'

