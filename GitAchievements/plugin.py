"""
Plugin interface.
"""

# pylint: disable=R0903

from GitAchievements.util import class_name

import collections
import imp
import os.path
import sets

class Plugin(object):
	"""
	Plugin interface base class.
	"""

	class TrackedInheritanceMeta(type):
		"""
		Meta class for tracking inheritance.
		"""

		__inheritors__ = collections.defaultdict(sets.Set)

		def __new__(mcs, name, bases, dct):
			"""
			Tracks all base classes on creation.
			"""

			cls = type.__new__(mcs, name, bases, dct)
			for base in cls.mro()[1:-1]:
				mcs.__inheritors__[class_name(base)].add(cls)

			return cls

	__metaclass__ = TrackedInheritanceMeta

	@classmethod
	def get_plugins(cls):
		"""
		Gets a list of all available achievements.
		"""

		return Plugin.__metaclass__.__inheritors__[class_name(cls)]

	@classmethod
	def get_plugin_by_name(cls, plugin_type):
		"""
		Get all plugins of type.

		Returns None if no plugin is found.
		"""

		if class_name(cls) not in Plugin.__metaclass__.__inheritors__:
			return None

		plugins = Plugin.__metaclass__.__inheritors__[class_name(cls)]
		for plugin in plugins:
			full_name = class_name(plugin)

			if full_name == plugin_type:
				return plugin

		return None

def load_plugins(plugin_dirs):
	"""
	Load the plugins from the plugin directories.
	"""

	for directory in plugin_dirs:
		load_plugins_from(directory)

	# TODO: finish?
	#for pkg in pkgutil.iter_modules(plugin_dirs):
		#print pkg
	#for module in pkgutil.walk_packages(plugin_dirs):
		#print module

def load_plugins_from(directory):
	"""
	Attempt to load plugins from the given directory.
	"""

	if not os.path.exists(directory):
		return

	files = os.listdir(directory)

	if '__init__.py' in files:
		dot_name = directory.replace(os.path.sep, '.')
		file_handle, filename, description = imp.find_module(
				os.path.basename(directory),
				[os.path.dirname(directory)])
		imp.load_module(dot_name, file_handle, filename, description)

	for plugin in files:
		if os.path.isdir(plugin):
			load_plugins_from(plugin)
			continue

		# We don't need to load compiled python files and other things.
		if not plugin.endswith('.py'):
			continue

		plugin_module = plugin[:-3]
		# TODO: this assumes that the path will use the system path character
		# TODO: will this cause problems with a plugin directory?
		dot_name      = os.path.join(directory, plugin_module).replace(os.path.sep, '.')

		file_handle, filename, description = imp.find_module(plugin_module, [directory])
		imp.load_module(dot_name, file_handle, filename, description)

