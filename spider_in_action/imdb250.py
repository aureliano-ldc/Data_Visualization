"""
抓取imdb250的电影目录
=====================
按电影出产年份绘制直方图

"""

import requests, re

from bs4 import BeautifulSoup

import pandas as pd
from pandas import DataFrame

import numpy as np

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

imdb250_url = 'http://www.imdb.com/chart/top'

names = []
ratings = []
years = []

# 定义抓取的函数
def retrieve_info(url):
	headers = {'User-Agent':
					'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
	data = requests.get(url, headers=headers).content
	soup = BeautifulSoup(data, 'html.parser')
	for item in soup.find_all('td', "titleColumn"):
		names.append(item.find('a').get_text(strip=True))
		years.append(item.find('span', 'secondaryInfo').get_text(strip=True).strip('()'))
	for imdbRating in soup.find_all('td', "ratingColumn imdbRating"):
		ratings.append(imdbRating.get_text(strip=True))
	

# 提取需要的数据
retrieve_info(imdb250_url)
# 修改ratings为浮点类型
ratings = list(map(float, ratings)) 

# 合并数据
movies = DataFrame({'rank': np.arange(1,251), 'names': names,
					'ratings': ratings, 'years': years})

# 按年份分组，加总排名和分数
mdf = movies.groupby('years').sum()
    
# 图像配置
my_config = pygal.Config()
my_config.x_label_rotation = 90
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18

my_style = LS('#333366', base_style=LCS)

# 生成Bar图
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'The weighted time-distribution of imdb250'
chart.x_labels = mdf.index
chart.add('', mdf['rank'])
chart.render_to_file('imdb250.svg')


# 让我们看看权重最高的1995年有哪些好电影
movies[movies.years == '1995']



