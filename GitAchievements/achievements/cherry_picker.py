"""
Cherry Picker
	Used git cherry-pick to add a sha from another branch into the current branch
"""

from GitAchievements.achievements import SingleUseAchievement

class CherryPickerAchievement(SingleUseAchievement):
	"""
	Cherry Picker
		Used git cherry-pick to add a sha from another branch into the current branch
	"""

	name        = 'Cherry Picker'
	description = 'Used git cherry-pick to add a sha from another branch into the current branch'
	cmd         = 'cherry-pick'

