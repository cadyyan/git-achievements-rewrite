"""
Unlockable achievements
"""

from GitAchievements.achievements.base import Achievement, UsageLeveledAchievement
from GitAchievements.achievements.architect import ArchitectAchievement
from GitAchievements.achievements.archivist import ArchivistAchievement
from GitAchievements.achievements.author import AuthorAchievement
from GitAchievements.achievements.blacksmith import BlacksmithAchievement
from GitAchievements.achievements.butcher import ButcherAchievement
from GitAchievements.achievements.carpenter import CarpenterAchievement
from GitAchievements.achievements.inventor import InventorAchievement
from GitAchievements.achievements.student import StudentAchievement

__all__ = [
	'Achievement',
	'ArchitectAchievement',
	'ArchivistAchievement',
	'BlacksmithAchievement',
	'ButcherAchievement',
	'CarpenterAchievement',
	'InventorAchievement',
	'StudentAchievement',
	'UsageLeveledAchievement',
]

