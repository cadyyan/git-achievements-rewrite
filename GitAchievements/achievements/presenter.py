"""
Presenter
	Shows one or more objects (blobs, trees, tags, and commits) with git show
"""

from GitAchievements.achievements import UsageLeveledAchievement

class PresenterAchievement(UsageLeveledAchievement):
	"""
	Presenter
		Shows one or more objects (blobs, trees, tags, and commits) with git show
	"""

	name        = 'Presenter'
	description = 'Shows one or more objects (blobs, trees, tags, and commits) with git show'
	cmd         = 'show .*(blobs|trees|tags|commits)'

