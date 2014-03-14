"""
Dentist
	Extracted patches using git-log -p
"""

from GitAchievements.achievements import SingleUseAchievement

class DentistAchievement(SingleUseAchievement):
	"""
	Dentist
		Extracted patches using git-log -p
	"""

	name        = 'Dentist'
	description = 'Extracted patches using git-log -p'
	cmd         = 'log .*-p'

