#!/usr/bin/python

# Libraries needed to do cool stuffs.
import feedparser
import math
from operator import itemgetter


class TFIDF(object):
	links = []
	terms = []
	term_amount = {}
	term_freq = {}
	total_terms = 0
	
	def __init__(self, url):
		self.url = url
		
		# Use feedparser to parse the content from the reddit rss feed
		self.parsed = feedparser.parse(self.url)
		
		# Go through the first 25 Links on given reddit page
		for x in range(1, 25):
			self.links.append(self.parsed.entries[x].title)
		
		# We populate the term frequency for the links of this subreddit here
		self.term_count()
		self.calc_tf()
	
	# Take our links and break them up into individual terms
	def convert_links_to_terms(self):
		for link in self.links:
			for term in link.split(' '):
				self.terms.append(term)
	
	# This method will count up the number of times a term appears and populate the term_freq dict
	def term_count(self):
		self.convert_links_to_terms()
		
		# Iterate through the terms we've collected for this subreddit, if their frequency is more
		# than twice, add them to the term frequency list, otherwise ignore them,
		for term in self.terms:
			self.term_amount[term] = self.terms.count(term)
			self.total_terms = self.total_terms + self.terms.count(term)
			
	# calculate the term weight
	def calc_tf(self):
		# We do the calculations to find the term frequency for each term here.
		for term in self.term_amount:
			self.term_freq[term] = float(self.term_amount[term])/float(self.total_terms)



proggit = TFIDF("http://www.reddit.com/r/programming.rss")
#for term in proggit.term_freq:
	#print term, ', ', proggit.term_freq[term]
#for term in proggit.term_freq
#	print term


#page2 = feedparser.parse("http://www.reddit.com/r/netsec.rss")
#for link in page2['entries']:
#	print link['title']    