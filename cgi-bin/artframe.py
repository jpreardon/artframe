#!/usr/bin/env python

import feedparser
import re
import json

# Define feeds here
feeds = ['http://formandalign.tumblr.com/rss', 'http://traceloops.tumblr.com/rss']

# List for image paths
imageList = []

# For each feed, parse it, and return all of the images
for feed in feeds:
	myFeed = feedparser.parse(feed)
	
	for item in myFeed.entries:
		# Get just the image path, and just get gifs
		images = re.findall(r'<img src="(.*gif)" />', item.description)

		for image in images:
			feedinfo = {'description':  myFeed.feed.subtitle, 'title': item.title, 'link': item.link, 'imagePath': image}
			imageList.append(feedinfo)

# Return JSON
output = "Content-Type: application/json\n\n"
output = output + json.dumps(imageList)
print output