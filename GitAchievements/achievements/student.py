"""
Student
	Accessed the documentation for a command with git [command] --help
"""

from GitAchievements.achievements.base import Achievement

class StudentAchievement(Achievement):
	"""
	Student
		Accessed the documentation for a command with git-[command] --help
	"""

	name        = 'Student'
	description = 'Accessed the documentation for a command with git [command] --help'

	@classmethod
	def check_condition(cls, app, command_args):
		for achiev in app.unlocked_achievements:
			if isinstance(achiev, cls):
				return None

		if len([arg for arg in command_args if arg == '--help' or arg == '-h']) >= 1:
			return StudentAchievement()

		return None

