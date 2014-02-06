# NewsTracker.py
# by Steven Liss

import os
import urllib
import workerpool

import urllib2
import re
from bs4 import BeautifulSoup
import urlparse
import time



class Result():
    def __init__(self, headline, url):
        self.headline = headline
        self.url = url
            




# return set of links, in output-ready format
def get_Links():
	def scrape(url):
		# for each site...

			t0 = time.time()
			print 'connecting to ' + url + '...'
			status_update = "   ..." + url + "   "
			try: # page may fail to load and throw an exception
				# get page's html
				page = urllib2.urlopen(url,timeout=30).read()
		
				#soup = BeautifulSoup(page)
				pages[url] = page
		
			except:
				t1 = time.time()
				print status_update + str("%0.2f" % (1000*(t1-t0))) + "ms -- COULD NOT LOAD PAGE"

			t1 = time.time()
			print status_update + 'complete --' + str("%0.2f" % (1000*(t1-t0))) + "ms"
		
	# Make a pool, five threads
	pool = workerpool.WorkerPool(size=10)
	pages = dict()
	results = set()
	
	# keys to search
	keys=list()
	raw_keys = [line.strip() for line in open('keys.txt')]

	# ensure keys are all lowercase
	for key in raw_keys:
		keys.append(key.lower())




	# list of sites to search
	url_list = [line.strip() for line in open('sites.txt')]

	# links that match a key
	matching_links = set()
	outputs = set()

	# for each site...
	# Perform the mapping
	pool.map(scrape, url_list)

	# Send shutdown jobs to all threads, and wait until all the jobs have been completed
	pool.shutdown()
	pool.wait()
	
	for k, value in pages.iteritems():
		#print value + '\n'
		soup = BeautifulSoup(value)
		#print soup
	
		raw_links = list()
		# add all <a> tags, and convert contents to lowercase
		for link in soup.find_all('a'):
			raw_links.append(link)
	
		# search each raw link for key, and add matches to matching_links
		for link in raw_links:
			match = 1 #start w/ assumption that link is a match
			for key in keys: # test each key; if it doesn't appear, set match to 0
				if not key in str(link).lower():
					match = 0
			if match == 1:
				full_link = urlparse.urljoin(k, str(link.get('href')))
				
				formatted_headline = ' '.join(link.get_text().split())
				if not formatted_headline: # blank headline
					formatted_headline = '<image link>'
			
				new_result = Result(formatted_headline,full_link)
			
				#if not new_result in results:
				#	print formatted_headline
				
				results.add(new_result)
				matching_links.add(full_link)
			
	# save found matches in text file
	found = open('found_stories.txt','w')

	for link in matching_links:
		found.write((link + '\n').encode('utf-8'))
	found.close()


	# output results header
	extant_headlines = set()
	for r in results:
		if not r.headline in extant_headlines:
			outputs.add(r)
		
		extant_headlines.add(r.headline)
		
	return outputs
