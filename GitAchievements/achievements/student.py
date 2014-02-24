"""
Student
	Accessed the documentation for a command with git [command] --help
"""

from GitAchievements.achievements.base import Achievement

import sys

class StudentAchievement(Achievement):
	"""
	Student
		Accessed the documentation for a command with git-[command] --help
	"""

	name        = 'Student'
	description = 'Accessed the documentation for a command with git [command] --help'

	@classmethod
	def check_condition(cls, app):
		for achiev in app.unlocked_achievements:
			if isinstance(achiev, cls):
				return None

		command_args = sys.argv[1:]

		if len([arg for arg in command_args if arg == '--help' or arg == '-h']) >= 1:
			return StudentAchievement()

		return None

