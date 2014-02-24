"""
Unlockable achievements
"""

from GitAchievements.achievements.base import Achievement, UsageLeveledAchievement
from GitAchievements.achievements.architect import ArchitectAchievement
from GitAchievements.achievements.archivist import ArchivistAchievement
from GitAchievements.achievements.carpenter import CarpenterAchievement
from GitAchievements.achievements.inventor import InventorAchievement
from GitAchievements.achievements.student import StudentAchievement

__all__ = [
	'Achievement',
	'ArchitectAchievement',
	'CarpenterAchievement',
	'InventorAchievement',
	'StudentAchievement',
	'UsageLeveledAchievement',
]

