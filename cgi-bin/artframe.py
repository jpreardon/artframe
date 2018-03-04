#!/usr/bin/env python

import feedparser
import re
import json

# Define feeds here
feeds = ['http://formandalign.tumblr.com/rss', 'http://traceloops.tumblr.com/rss']

# List for image paths
imagePaths = []

# For each feed, parse it, and return all of the images
for feed in feeds:
	myFeed = feedparser.parse(feed)
	
	for item in myFeed.entries:
		# Get just the image path, and just get gifs
		images = re.findall(r'<img src="(.*gif)" />', item.description)

		for image in images:
			imagePaths.append(image)

# Return JSON
output = "Content-Type: application/json\n\n"
output = output + json.dumps(imagePaths)
print output