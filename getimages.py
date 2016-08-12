#!/usr/bin/env python

# before run add BING_API_KEY variable to env like
# export BING_API_KEY='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

import os
from py_bing_search import PyBingImageSearch
filter = 'Size:medium+Color:Monochrome'
filter = 'Face:Face'
bing_image = PyBingImageSearch(os.environ['BING_API_KEY'], "woman", image_filters=filter) #image_filters is optional
first_fifty_result= bing_image.search(limit=1000, format='json') #1-50

for res in (first_fifty_result):
	print res.media_url

# second_fifty_result= bing_image.search(limit=50, format='json') #51-100
# for res in (second_fifty_result):
# 	print res.media_url

