"""
Cathedral Worker
	Cloned submodule repository and checked out commits specified by super project
"""

from GitAchievements.achievements import SingleUseAchievement

class CathedralWorkerAchievement(SingleUseAchievement):
	"""
	Cathedral Worker
		Cloned submodule repository and checked out commits specified by super project
	"""

	name        = 'Cathedral Worker'
	description = 'Cloned submodule repository and checked out commits specified by super project'
	cmd         = 'submodule update'

