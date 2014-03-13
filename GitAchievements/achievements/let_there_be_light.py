"""
Let There Be Light
	Commit without a parent
"""

import re

from GitAchievements.achievements import Achievement

class LetThereBeLightAchievement(Achievement):
	"""
	Let There Be Light
		Commit without a parent
	"""

	name = 'Let There Be Light'
	description = 'Commit without a parent'

	@classmethod
	def check_condition(cls, app, command_args):
		if not re.search('commit', ' '.join(command_args)):
			return None

		if len(app.git.log('--pretty=oneline').split('\n')) != 1:
			return None

		return cls()

