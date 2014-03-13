"""
Cathedral Architect
	Added a submodule to a repository
"""

from GitAchievements.achievements import SingleUseAchievement

class CathedralArchitectAchievement(SingleUseAchievement):
	"""
	Cathedral Architect
		Added a submodule to a repository
	"""

	name        = 'Cathedral Achitect'
	description = 'Added a submodule to a repository'
	cmd         = 'submodule add'

