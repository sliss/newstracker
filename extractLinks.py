import urllib2
import re

page = urllib2.urlopen('http://www.google.com').read()

urls = list()

def extract_urls(page):
    url_re = re.compile(r'\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))')
    for match in url_re.finditer(page):
        yield match.group(0)

for uri in extract_urls(page):
    urls.append(uri)
    
for happystring in urls:
    print happystring

