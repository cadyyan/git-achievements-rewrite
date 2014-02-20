"""
HTML and RSS based publisher.
"""

from GitAchievements.publisher.base import Publisher

import jinja2
import os.path
import re

class HtmlPublisher(Publisher):
	"""
	HTML and RSS based publisher.
	"""

	def __init__(self, app):
		"""
		Sets up the HTML and RSS publisher.
		"""

		super(HtmlPublisher, self).__init__(app)

		self.html_template = self.config.get_value(
				'achievement', 'publisher_html_template_html',
				default = 'original.html')

		self.rss_template = self.config.get_value(
				'achievement', 'publisher_html_template_rss',
				default = 'original.rss')

		self.jinja_env = jinja2.Environment(
				loader = jinja2.FileSystemLoader(os.path.join(app.achievements_dir, 'templates')))

		self.jinja_env.filters['regex_replace'] = regex_replace

	def publish(self, app):
		"""
		Publish achievements to an HTML file and an RSS file.
		"""

		context = {
			'all_achievements': app.all_achievements,
			'unlocked_achievements': app.unlocked_achievements,
			'locked_achievements': [
				a for a in app.locked_achievements if a not in app.unlocked_achievements
			],
			'points': app.get_points(),
		}

		for section in self.config.sections():
			data = {}
			for option in self.config.options(section):
				data[option] = self.config.get_value(section, option)

			context[section] = data

		html_template = self.jinja_env.get_template(self.html_template)
		rss_template  = self.jinja_env.get_template(self.rss_template)

		html = html_template.render(context)
		rss  = rss_template.render(context)

		html_file = os.path.join(app.achievements_dir, 'index.html')
		rss_file  = os.path.join(app.achievements_dir, 'index.rss')

		with open(html_file, 'w') as html_fh:
			html_fh.write(html)

		with open(rss_file, 'w') as rss_fh:
			rss_fh.write(rss)

		return [html_file, rss_file]

def regex_replace(value, regex, replace):
	"""
	Jinja tag similar to the built-in replace but takes a regex.
	"""

	return re.sub(regex, replace, value)

