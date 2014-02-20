"""
Data stores
"""

from GitAchievements.store.base import Store
from GitAchievements.store.file import LogFileStore

__all__ = [
	'LogFileStore',
	'Store',
]

