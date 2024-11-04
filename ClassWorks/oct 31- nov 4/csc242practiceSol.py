# CSC 242
# Practice questions solutions

from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse

# Problem 1: Limited-recursion crawler
class Crawler(object):
    def __init__(self):
        self.visited = set()

    def reset(self):
        self.visited = set()
            
    def crawl(self, url, depth):
        self.visited.add(url)
        links = self.analyze(url)
        if depth > 0:
            for link in links:
                if link not in self.visited:
                    try:
                        self.crawl(link, depth-1)
                    except:
                        pass
                
    def analyze(self, url):
        print("Visiting ", url)
        content = urlopen(url).read().decode()
        collector = Collector(url)
        collector.feed(content)
        urls = collector.getLinks()
        return urls

# Problem 2: Breadth-first crawler
class Crawler2(object):
    def __init__(self):
        'constructor'
        self.discovered = set()

    def reset(self):
        'reset the visited links'
        self.discovered = set()

    # Write this function
    # It will NOT be recursive
    def crawl(self, startURL):
        'breadth-first search web crawler'
        urlsToVisit = queue()
        urlsToVisit.enqueue(startURL)
        self.discovered.add(startURL)   

        while not urlsToVisit.isEmpty():
            url = urlsToVisit.dequeue()
            try:
                links = self.analyze(url)          
                for link in links:
                    if link not in self.discovered:
                        urlsToVisit.enqueue(link)
                        self.discovered.add(link)
            except:
                pass

    def analyze(self, url):
        'returns the list of URLs found in the page url'
        print("Visiting", url)
        content = urlopen(url).read().decode()
        collector = Collector(url)
        collector.feed(content)
        urls = collector.getLinks()
        return urls

# Helper classes for the breadth-first crawler
# Do not modify
class queue(object):
    def __init__(self):
        'the constructor'
        self.q = list()
        
    def dequeue(self):
        'removes and returns the first item in the queue'
        assert self.isEmpty() == False, f"Cannot dequeue from an empty queue"
        return self.q.pop(0)
    
    def enqueue(self, item):
        'add item to the back of the queue'
        self.q.append(item)
    
    def size(self):
        'returns the number of items in the queue'
        return len(self.q)
    
    def isEmpty(self):
        'return True if the queue is empty'
        return self.size() == 0
    
    def __repr__(self):
        'the representation'
        return repr(self.q)
    
    def __str__(self):
        'the string representation'
        theq = ''
        for index in range(len(self.q)):
            theq += str(self.q[index]) + "\n"
        theq = theq.strip()
        return theq

    def __iter__(self):
        'the iterator'
        return iter(self.q)
    
class Collector(HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a':
            for att in attrs:
                if att[0].lower() == 'href':
                    if not att[1].lower().startswith('mailto:'):
                        self.links.append(urljoin(self.url, att[1]))

    def getLinks(self):
        return self.links
