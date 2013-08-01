import urllib2
import re

#seed = urllib2.urlopen('http://www.udacity.com/cs101x/index.html').read()
seed = 'http://www.udacity.com/cs101x/index.html'
#seed = 'http://cs101.udacity.com/urank/index.html'

# takes a url as input, extract all urls from the input's web page
def extract_urls(page):
    html = urllib2.urlopen(page).read()
    #url_re = re.compile(r'\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))')
    url_re = re.compile(r'(?<=href=").*?(?=")')
    for match in url_re.finditer(html):
        yield match.group(0)
        
def get_links(page):
    links = list()
    for uri in extract_urls(page):
        links.append(uri)
    return links

def add_page_to_graph(graph, url):
    graph[url].append(get_links(url))
    
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    graph = {}
    index = {}
    links = list()
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            add_page_to_index(index, page)
            links = get_links(page)
            graph[page]=links
            union(tocrawl, links) # add new links to tocrawl
            crawled.append(page)
    return index, graph

def add_to_index(index, keyword, url):
    if keyword in index:
            index[keyword].append(url)
    else: # keyword not in index yet; add new keyword to index
        index[keyword] = [url]    
        
def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url):
    content = urllib2.urlopen(url).read()
    text = content.split()
    for word in text:
        add_to_index(index, word, url)

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages # starting rank = 1 /# of pages indexed
    
    for i in range(0, numloops): # iterate through graph i times...
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph: # go through each node...
                if page in graph[node]: # if node has a link to current page...
                    newrank += d * (ranks[node] / len(graph[node])) # page's new rank increased by (node's rank / node's # of outbound links)
            newranks[page] = newrank
        ranks = newranks
    return ranks

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

index, graph = crawl_web(seed)
ranks = compute_ranks(graph)

print ranks
#print lookup(index,'magic')