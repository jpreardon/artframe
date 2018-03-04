# Artframe Worklog

## 2018-03-03

Basically, we want a photo frame type thing that cycles through images that have been posted to one or more RSS feed (from Tumblr at the moment).

Figured out how it might work:

- Python RSS parser goes through each feed, returns JSON with a list of the images
- Webpage with javascript that calls the aforementioned RSS parser and displays one image at a time, randomly.
- Once in a while, the webpage should refresh from the python script

Super basic. Sure, there could be caching, but we'll ignore that for now and just try to get stuff running.

Using [feedparser](https://github.com/kurtmckee/feedparser/tree/5.2.0) to parse the feeds.