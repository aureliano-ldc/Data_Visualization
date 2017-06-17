"""
抓取Hacker News 上评论最多的文章
==================================
教程来自：《Python_Crash_Course》

"""

import requests

from operator import itemgetter

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
	# Make a separate API call for each submission.
	url = ('https://hacker-news.firebaseio.com/v0/item/' + 
			str(submission_id) + '.json')
	submission_r = requests.get(url)
	print(submission_r.status_code)
	response_dict = submission_r.json()

	submission_dict = {
		'title': response_dict['title'],
		'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
		'comments': response_dict.get('descendants', 0)
		}
	submission_dicts.append(submission_dict)

"""
We want to sort the list of dictionaries by the number of comments. To do
this, we use a function called itemgetter() {, which comes from the operator
module. We pass this function the key 'comments', and it pulls the value associated
with that key from each dictionary in the list. The sorted() function
then uses this value as its basis for sorting the list.
"""
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
							reverse=True)

for submission_dict in submission_dicts:
	print("\nTitle:", submission_dict['title'])
	print("Discussion link:", submission_dict['link'])
	print("Comments:", submission_dict['comments'])
