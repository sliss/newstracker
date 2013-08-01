import urllib2
import re

#seed = urllib2.urlopen('http://www.udacity.com/cs101x/index.html').read()
seed = 'http://www.udacity.com/cs101x/index.html'

# takes a url as input, extract all urls from the input's web page
def extract_urls(page):
    html = urllib2.urlopen(page).read()
    #url_re = re.compile(r'\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))')
    url_re = re.compile(r'(?<=href=").*?(?=")')
    for match in url_re.finditer(html):
        yield match.group(0)

    
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            for uri in extract_urls(page):
                tocrawl.append(uri)
            crawled.append(page)
    return crawled

print crawl_web(seed)