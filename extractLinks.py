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

print("SEARCHING FOR:")
for key in keys:
	print key;

# list of sites to search
url_list = [line.strip() for line in open('sites.txt')]

# links that match a key
matching_links = list()
soups = list()

# output results header
print("\nRESULTS")

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
				full_link =urlparse.urljoin(url, str(link.get('href')))
				output += full_link
				output = ' '.join(output.split())
				print output
				matching_links.append(full_link)
				
# save found matches in text file
found = open('found_stories.txt','w')

for link in matching_links:
	found.write((link + '\n').encode('utf-8'))

found.close()



#for link in matching_links:
#	print ' '.join(link.split())
