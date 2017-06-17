import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

from random import randint

# 先稍微学习一下如何构建条形图：
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
	{'value': 16101, 'label': 'Description of httpie.'},
	{'value': 15028, 'label': 'Description of django.'},
	{'value': 14798, 'label': 'Description of flask.'},
	]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')




# Roll点频率统计：
class Die():
	"""A class representing a single die."""

	def __init__(self, num_sides=6):
		"""Assume a six-sided die."""
		self.num_sides = num_sides

	def roll(self):
		"""Return a random value between a and number of sides."""
		return randint(1, self.num_sides)


# Create a D6 dice and a D10 dice.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
# Roll点50000次，记录每次相加的点数。
results = []
for roll_num in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 50000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
	'13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frenquency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')

