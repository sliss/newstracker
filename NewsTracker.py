# NewsTracker.py
# by Steven Liss

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
	for url in url_list:
		#try: # page may fail to load and throw an exception
			# get page's html
		page = urllib2.urlopen(url).read()


		soup = BeautifulSoup(page)
		raw_links = list()
		# add all <a> tags, and convert contents to lowercase
		for link in soup.find_all('a'):
			raw_links.append(link)

		# search each raw link for key, and add matches to matching_links
		for link in raw_links:
			for key in keys:
				if key in str(link).lower():
					full_link = urlparse.urljoin(url, str(link.get('href')))
					
					formatted_headline = ' '.join(link.get_text().split())
					if not formatted_headline: # blank headline
						formatted_headline = '<image link>'
						
					results.add(Result(formatted_headline,full_link))
					matching_links.add(full_link)
		#except:
		#	print 'could not load page'
			
			
	# save found matches in text file
	found = open('found_stories.txt','w')

	for link in matching_links:
		found.write((link + '\n').encode('utf-8'))
	found.close()


	# output results header
	return results
