"""
Carpenter Achievement:
	Custom git hooks are installed which helps catch issues before they are shared.
"""

from GitAchievements.achievements.base import Achievement

import os
import os.path

class CarpenterAchievement(Achievement):
	"""
	Carpenter Achievement:
		Custom git hooks are installed which helps catch issues before they are shared.
	"""

	name        = 'Carpenter'
	description = 'Custom git hooks are installed which helps catch issues before they are shared.'

	@classmethod
	def check_condition(cls, app, command_args):
		if not app.repo:
			return False

		hooks_dir = os.path.join(app.repo.git_dir, 'hooks')

		hooks        = os.listdir(hooks_dir)
		active_hooks = [hook for hook in hooks if not hook.endswith('sample')]

		current_level = app.get_current_level(CarpenterAchievement.name)

		if len(active_hooks) < 1 or hooks < current_level:
			return None

		# Just for completeness make sure to unlock any levels between the current level
		# and the new level.
		return [CarpenterAchievement(level = i + 1) for i in range(current_level, hooks)]

