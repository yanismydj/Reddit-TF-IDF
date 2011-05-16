#!/usr/bin/python

# Libraries needed to do cool stuffs.
import feedparser

class tfidf(object):
	links1 = []
	links2 = []
	
	def __init__(self, url1, url2):
		self.url1 = url1
		self.url2 = url2
		
		self.parsed1 = feedparser.parse(self.url1)
		self.parsed2 = feedparser.parse(self.url1)

		for x in range(1, 25):
			self.links1.append(self.parsed1.entries[x].title)
   			self.links2.append(self.parsed2.entries[x].title)    

    def linkcompare(self):
        print self.links

		

	
proggit = tfidf("http://www.reddit.com/r/programming.rss", "http://www.reddit.com/r/netsec.rss")
print proggit.links1
print proggit.links2
proggit.linkcompare()


#page2 = feedparser.parse("http://www.reddit.com/r/netsec.rss")
#for link in page2['entries']:
#	print link['title']    