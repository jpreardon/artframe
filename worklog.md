# Artframe Worklog

## 2018-03-03

Basically, we want a photo frame type thing that cycles through images that have been posted to one or more RSS feed (from Tumblr at the moment).

Figured out how it might work:

- Python RSS parser goes through each feed, returns JSON with a list of the images
- Webpage with javascript that calls the aforementioned RSS parser and displays one image at a time, randomly.
- Once in a while, the webpage should refresh from the python script

Super basic.

Using [feedparser](https://github.com/kurtmckee/feedparser/tree/5.2.0) to parse the feeds. I installed it locally, but my shared server didn't have it, so I just stuck the module in the cgi-bin directory.

I forgot that one needs to tell the [server to execute python scripts](https://stackoverflow.com/questions/6351028/how-to-execute-python-cgi-script).

The javascript is pretty hacky, but it works as a POC, even if the POC is a bit of a POS :P