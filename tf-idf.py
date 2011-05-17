#!/usr/bin/python

# Libraries needed to do cool stuffs.
import feedparser
import math
import operator

# List of subreddits for our sample
subreddits = ['atheism', 'soccer', 'atheism', 'LosAngeles', 'pics', 'funny', 'politics', 'gaming']

# This is the list we'll use to store ALL the terms from Every subreddit
all_terms = {}

# Holds subreddit attributes/methods
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
			
			
def calc_tfidf(term, subreddit_parent, document_objs):
	term_appears = 0
	for subreddit in all_terms:
		if document_objs[subreddit].contains_the_term(term):
			term_appears += 1
	
	idf = math.log(len(document_objs) / term_appears)
	tfidf = idf * document_objs[subreddit_parent].term_freq[term]
	
	return tfidf

reddit_list = {}
top_terms_global = []
term_scores = {}

for subreddit in subreddits:
	reddit_list[subreddit] = SubRedditObj(subreddit)

for subreddit in subreddits:
	for term in reddit_list[subreddit].top_items_sorted:
		tfidf_score = calc_tfidf(term[0], subreddit, reddit_list)
		term_scores[term[0]] = tfidf_score

term_scores_sorted = sorted(term_scores.iteritems(), key=operator.itemgetter(1))

for scored_term in term_scores_sorted:
	print scored_term[0], ' has a score of ', "%.6f" % scored_term[1]

 