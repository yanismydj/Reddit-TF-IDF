#!/usr/bin/python

# Libraries needed to do cool stuffs.
import feedparser
import math
import operator
from random import choice

all_terms = {}

# List of subreddits for our sample
subreddits = ['atheism', 'soccer', 'atheism', 'LosAngeles', 'pics', 'funny', 'politics', 'gaming',
'worldnews', 'askreddit', 'videos', 'iama', 'todayilearned', 'AdviceAnimals', 'starcraft', 'WTF', 
'fffffffuuuuuuuuuuuu']



# Holds subreddit attributes/methods.  Subreddit is interchangable with document for this assignment
class SubRedditObj(object):
	
	def __init__(self, subreddit):
		self.subreddit = subreddit
		self.url = "http://www.reddit.com/r/%s.rss" % (subreddit)
		all_terms[self.subreddit] = []
		self.term_idfs = {}
		self.total_terms = 0
		
		# Call Getter method to pull up the objects data
		self._getter()
		
		
		# Go through the first 25 Links on given reddit page
		self.links = []

		for x in range(1, 25):
			self.links.append(self.parsed.entries[x].title)
		
		# We populate the term frequency for the links of this subreddit here
		self._term_count()
		self.calc_tf()
		
		# Calculate the top terms
		self._top_terms()
	
	# breaking this into its own method, in case we wish to save to file or such.
	def _getter(self):
		# Use feedparser to parse the content from the reddit rss feed
		self.parsed = feedparser.parse(self.url)
	
	
	# Take our links and break them up into individual terms
	def _convert_links_to_terms(self):
		self.terms = []
		for link in self.links:
			for term in link.split(' '):
				self.terms.append(term.lower())
	
	
	# This method will count up the number of times a term appears and populate the term_freq dict
	def _term_count(self):
		self._convert_links_to_terms()
		self.term_amount = {}

		# Iterate through the terms we've collected for this subreddit, if their frequency is more
		# than twice, add them to the term frequency list, otherwise ignore them
		for term in self.terms:
			self.term_amount[term] = self.terms.count(term)
			self.total_terms = self.total_terms + self.terms.count(term)
	
	
	# calculate the term weight
	def calc_tf(self):
		self.term_freq = {}

		# We do the calculations to find the term frequency for each term here.
		for term in self.term_amount:
			self.term_freq[term] = float(self.term_amount[term])/float(self.total_terms)

	
	# this is a function to display the top terms for this reddit, sorted by appearance
	def _top_terms(self):
		self.top_items = {}
		
		# For this assignment, we'll limit the top terms to terms who appear more than once
		for term in self.term_amount:
			if self.term_amount[term] > 1:
				self.top_items[term] = self.term_amount[term]
				
		# Sorted tuples
		self.top_items_sorted = sorted(self.top_items.iteritems(), key=operator.itemgetter(1))
		self.top_items_sorted.reverse()
	
	
	# Find out if this document contains a given term
	def contains_the_term(self, term_input):
		# Check to see if a term appears in this object
		try:
			return self.terms.index(term_input)
		except:
			return False



# This class helps calculate the tfidf scores once we've laid all the ground work.  It also allows
# us to represent our tfidf weights in interesting ways
class TfidfScores(object):
	
	def __init__(self, subreddits):
		self.subreddits = subreddits
		self.reddit_list = {}
		self.top_terms_global = []
		self.scores = []
		
		# populate reddit_list( list of subreddit objects)
		self.reddit_list = self.get_subreddit_objects(self.subreddits)
		
		# populate scores
		self.scores = self.build_tfidf_scores()
	
	
	# Method to build the reddit_list of objects for our given list of subreddits
	def get_subreddit_objects(self, subreddits):
		reddit_list = {}
		for subreddit in subreddits:
			reddit_list[subreddit] = SubRedditObj(subreddit)
			
		return reddit_list
	
	
	# This function will build the top tfidf scores for each subreddit
	def build_tfidf_scores(self):
		scores = []
		for subreddit in self.subreddits:
			for term in self.reddit_list[subreddit].top_items_sorted:
				if (self._calc_tfidf(term[0], subreddit) > 0):
					term_score = [term, subreddit, self._calc_tfidf(term[0], subreddit)]
					scores.append(term_score)
		return scores
	

	# the heavy lifting to calculate a tfidf score
	def _calc_tfidf(self, term, subreddit_parent):
		term_appears = 0
		for subreddit in all_terms:
			if self.reddit_list[subreddit].contains_the_term(term):
				term_appears += 1
		
		if term_appears > 0:
			idf = math.log(len(self.reddit_list) / term_appears)
			tfidf = idf * self.reddit_list[subreddit_parent].term_freq[term]
		else:
			tfidf = 0
		
		return tfidf


	def what_do_they_like(self):
		rand = choice(self.scores)
		return "People from %s probably like %s (tf-idf weight of %.9f)" % (rand[1], rand[0][0], rand[2])


tfidfs = TfidfScores(subreddits)

print tfidfs.what_do_they_like()

