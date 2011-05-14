#!/usr/bin/python

# Libraries needed to do cool stuffs.
import urllib
import htmlparser

# Get a page
page1 = "http://www.reddit.com/r/programming"
socket = urllib.urlopen(page1)
r_programming_html = socket.read()
socket.close()


# Get a page
#page2 = "http://www.reddit.com/r/netsec"
#socket = urllib.urlopen(page2)
#page2 = socket.read()
#socket.close()        


# Parse the HTML
page1_parser = htmlparser()

page1_parser.feed(html)