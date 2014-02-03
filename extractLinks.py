import urllib2
import re
from bs4 import BeautifulSoup


# keys to search
keys = list()

keys.append('albert'.lower())
keys.append('IMAGE'.lower())
keys.append('sign'.lower())

for key in keys:
	print key;


# get page's html
page = urllib2.urlopen('http://www.google.com').read()
soup = BeautifulSoup(page)

raw_links = list()
matching_links = list()

# add all a tags, and convert contents to lowercase
for link in soup.find_all('a'):
	raw_links.append(link)

# search each raw link for key, and add matches to matching_links
for link in raw_links:
    for key in keys:
    	if key in str(link).lower():
    		matching_links.append(link)

for link in raw_links:
	print link;

print("RESULTS")

for link in matching_links:
	s = link.get_text() + ': ' + str(link.get('href'));
	print s
#soup.find_all(a=re.compile("elsie"))


    
'''
def extract_urls(page):
    url_re = re.compile(r'\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))')
    for match in url_re.finditer(page):
        yield match.group(0)

for uri in extract_urls(page):
    urls.append(uri)
    


'''

