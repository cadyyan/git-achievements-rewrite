"""
Helpful utility methods!
"""

import os.path

def expand_filepath(path):
	"""
	Expands a file path to include system variables.
	"""

	return os.path.expanduser(os.path.expandvars(path))

def class_name(obj):
	"""
	Gets the class name of a class object.
	"""

	return obj.__module__ + '.' + obj.__name__

