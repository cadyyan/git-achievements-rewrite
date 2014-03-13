"""
Librarian
	Looked for change that introduce or remove a string with git-log -S
"""

from GitAchievements.achievements import SingleUseAchievement

class LibrarianAchievement(SingleUseAchievement):
	"""
	Librarian
		Looked for change that introduce or remove a string with git-log -S
	"""

	name        = 'Librarian'
	description = 'Looked for a change that introduce or remove a string with git-log -S'
	cmd         = 'log .*-S'

