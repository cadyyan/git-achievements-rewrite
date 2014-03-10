"""
Baptised
	Set global user name using git config
"""

from GitAchievements.achievements import Achievement

class BaptisedAchievement(Achievement):
	"""
	Baptised
		Set global user name using git config
	"""

	name        = 'Baptised'
	description = 'Set global user name using git config'

	@classmethod
	def check_condition(cls, app):
		usage = app.store.get_usage_count('config --global user.name')
		if usage == 0:
			return None

		if len([a for a in app.unlocked_achievements if a.name == cls.name]) > 0:
			return None

		return cls()

