#!/usr/bin/python

# Libraries needed to do cool stuffs.
import feedparser
import math
from operator import itemgetter

# List of subreddits for our sample
subreddits = ['atheism', 'soccer', 'atheism', 'LosAngeles', 'pics', 'funny', 'politics', 'gaming']

# This is the list we'll use to store ALL the terms from Every subreddit
all_terms = {}

class TFIDF(object):
	links = []
	terms = []
	term_amount = {}
	term_freq = {}
	term_idfs = {}
	total_terms = 0
	
	def __init__(self, subreddit):
		self.subreddit = subreddit
		self.url = "http://www.reddit.com/r/%s.rss" % (subreddit)
		all_terms[self.subreddit] = []
		
		
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
				#all_terms.append(term)
	
	# This method will count up the number of times a term appears and populate the term_freq dict
	def term_count(self):
		self.convert_links_to_terms()
		
		# Iterate through the terms we've collected for this subreddit, if their frequency is more
		# than twice, add them to the term frequency list, otherwise ignore them
		for term in self.terms:
			self.term_amount[term] = self.terms.count(term)
			self.total_terms = self.total_terms + self.terms.count(term)
			
			# Now add this to our all_terms dict, but only if they appear more than once
			if self.terms.count(term) > 1:
				print term, ' => ', self.terms.count(term)
#				all_terms[self.subreddit][term] = self.terms.count(term)
			
	# calculate the term weight
	def calc_tf(self):
		# We do the calculations to find the term frequency for each term here.
		for term in self.term_amount:
			self.term_freq[term] = float(self.term_amount[term])/float(self.total_terms)
	
	# Calculate the inverse document frequency
	def calc_idf(self, subreddit_obj):
		# Here we are going to do the math to find the weight of terms by comparing another subreddit
		# object
		for term in self.terms:
			if (subreddit_obj.contains_the_term(term)):	
				idf = math.log(2)
	
	# Find out if this document contains a given term
	def contains_the_term(self, term_input):
		# Check to see if a term appears in this object
		try:
			return self.terms.index(term_input)
		except:
			return False

reddit = {}
for subreddit in subreddits:
	reddit[subreddit] = TFIDF(subreddit)

for subreddit in all_terms:
	print subreddit


#proggit = TFIDF("http://www.reddit.com/r/programming.rss")

#print proggit.contains_the_term("Asynchronous")

#print proggit.terms.index()
#	print 'true'
#else:
#	print 'false'
#for term in proggit.term_freq:
#	print term, ', ', proggit.term_freq[term]
#for term in proggit.term_freq
#	print term


#page2 = feedparser.parse("http://www.reddit.com/r/netsec.rss")
#for link in page2['entries']:
#	print link['title']    