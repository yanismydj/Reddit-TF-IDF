#!/usr/bin/python

# Libraries needed to do cool stuffs.
#import urllib
import feedparser

# Get a feed (deprecated when moving to feedparser method)
#page1 = "http://www.reddit.com/r/programming.rss"
#socket = urllib.urlopen(page1)
#page1_html = socket.read()
#socket.close()


              
page1 = feedparser.parse("http://www.reddit.com/r/programming.rss")
#print page1['entries'][0]['title'] <- Link title, what we want
for link in page1['entries']:
	print link['title']

page2 = feedparser.parse("http://www.reddit.com/r/netsec.rss")
for link in page2['entries']:
	print link['title']    