import urllib2
import re
from bs4 import BeautifulSoup
import urlparse


# keys to search

keys=list()
raw_keys = [line.strip() for line in open('keys.txt')]

# ensure keys are all lowercase
for key in raw_keys:
	keys.append(key.lower())

for key in keys:
	print key;

# list of sites to search
url_list = [line.strip() for line in open('sites.txt')]

# links that match a key
matching_links = list()
soups = list()

# output results header
print("RESULTS")

# for each site...
for url in url_list:

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
				output = link.get_text();
				output += ': '
				output +=urlparse.urljoin(url, str(link.get('href')))
				matching_links.append(output)
				

'''
	for link in raw_links:
		print link;
'''



for link in matching_links:
	print ' '.join(link.split())
