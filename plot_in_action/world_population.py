"""
数据地图——世界人口分布
======================
教程来自：《Python_Crash_Course》

"""

import json

from pygal_maps_world.maps import World
from pygal.style import LightColorizedStyle, RotateStyle

from pygal_maps_world.i18n import COUNTRIES


# 获取城市代码
def get_country_code(country_name):
	"""Return the Pygal 2-digit country code for the given country."""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
	# If the country wasn't found, return None.
	return None


# Load the data into a list.
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)


# Print the 2010 population for each country.
cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country)
		if code:
			cc_populations[code] = population

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop


# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('C:/Users/Administrator/world_population.svg')