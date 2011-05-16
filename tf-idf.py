#!/usr/bin/python

# Libraries needed to do cool stuffs.
import feedparser
import math

class tfidf(object):
	links = []
	terms = []
	
	def __init__(self, url):
		self.url = url
		
		self.parsed = feedparser.parse(self.url)
		
		# Go through the first 25 Links on given reddit page
		for x in range(1, 25):
			self.links.append(self.parsed.entries[x].title)
	
	def convert_links_to_terms(self):
		for link in self.links:
			self.terms.append(link.split(' '))
	
	def term_count(self):
		self.tf = count(terms)
		

	
proggit = tfidf("http://www.reddit.com/r/programming.rss")
print proggit.links
proggit.convert_links_to_terms()
print proggit.terms


#page2 = feedparser.parse("http://www.reddit.com/r/netsec.rss")
#for link in page2['entries']:
#	print link['title']    