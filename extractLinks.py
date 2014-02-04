import urllib2
import re
from bs4 import BeautifulSoup
import urlparse
import time

'''
class Result():
    def __init__(self, url, text):
        self.url = url
        self.text = text
'''

# keys to search

keys=list()
raw_keys = [line.strip() for line in open('keys.txt')]

# ensure keys are all lowercase
for key in raw_keys:
	keys.append(key.lower())

print("SEARCHING FOR:")
for key in keys:
	print key;

print("\nSCANNING...")
# list of sites to search
url_list = [line.strip() for line in open('sites.txt')]
print url_list

# links that match a key
matching_links = set()
outputs = set()



# for each site...
for url in url_list:
	t0 = time.time()
	status_update = "   ..." + url + "   "
	try: # page may fail to load and throw an exception
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
					#results.add(Result(urlparse.urljoin(url, str(link.get('href'))),link.get_text()))
					output = link.get_text();
					output += ': '
					full_link =urlparse.urljoin(url, str(link.get('href')))
					output += full_link
					output = ' '.join(output.split())
					outputs.add(output)
					matching_links.add(full_link)
	except:
		t1 = time.time()
		print status_update + str("%0.2f" % (1000*(t1-t0))) + "ms -- COULD NOT LOAD PAGE"
	
	t1 = time.time()
	print status_update + str("%0.2f" % (1000*(t1-t0))) + "ms"
				
				
# save found matches in text file
found = open('found_stories.txt','w')

for link in matching_links:
	found.write((link + '\n').encode('utf-8'))
found.close()


# output results header

print "\nRESULTS:"

for o in outputs:
	print o
