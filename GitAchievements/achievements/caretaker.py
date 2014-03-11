"""
Caretaker
	Added a .gitignore file to a repository
"""

from GitAchievements.achievements import SingleUseAchievement

class CaretakerAchievement(SingleUseAchievement):
	"""
	Caretaker
		Added a .gitignore file to a repository
	"""

	name        = 'Caretaker'
	description = 'Added a .gitignore file to a repository'
	cmd         = r'add .*\.gitignore'

