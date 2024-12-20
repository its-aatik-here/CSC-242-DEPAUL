# If you're using a Mac and having trouble,
# uncomment this code:
##ctx = ssl.create_default_context()
##ctx.check_hostname = False
##ctx.verify_mode = ssl.CERT_NONE
# Then change the second line in analyze to this:
#content = urlopen(url, context=ctx).read().decode()

from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen


# Change this to import from whatever file holds the Collector class
from moreHTMLParsers import Collector

class Crawler(object):
        
    def crawl(self, url):
        ' recursive web crawler that calls analyze() on each web page'
        links = self.analyze(url)
        for link in links:
            try:
                self.crawl(link)
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
