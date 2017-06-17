"""
抓取GitHub上面最多星的项目
==========================
教程来自：《Python_Crash_Course》

"""

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers = {'User-Agent':
					'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
# 发现模拟火狐浏览器请求是最快的
r = requests.get(url, headers=headers)

# A status code of 200 indicates a successful response.
print("Status code:", r.status_code)

# Store API response in avariable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
	# 处理存在的Na值，不然作图会报错
	if repo_dict['description'] == None:
		repo_dict['description'] = 'No description'
	names.append(repo_dict['name'])
	plot_dict = {
		'value': repo_dict['stargazers_count'],
		'label': repo_dict['description'],
		'xlink': repo_dict['html_url']
		}
	plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
# Use truncate_label to shorten the longer project names to 15 characters.
my_config.truncate_label = 15
# Hide the horizontal lines on the graph.
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

