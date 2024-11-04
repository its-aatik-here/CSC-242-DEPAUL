import code 
import os

from html.parser  import HTMLParser
class DataCollector (HTMLParser):
    def __init__ (self):
        HTMLParser.__init__ (self)
        self.accumulator = []
    def  handle_starttag (self, tag, attrs):
        pass
    def handle_data(self, data):
        self.accumulator.append(data)
    def handle_endtag (self,tag):
        pass
    def getData (self):
        res = ""
        for item in self.accumulator:
            res += item
        return res
    


class HeaderParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.headings = []
        self.inheader = False
        self.nestedP =  False

    def  handle_starttag(self, tag, attrs):
        if tag in  ['h1', 'h2', 'h3', 'h4', 'h5',"h6"]:
            self.inheader = True
        elif  tag == 'p' and self.inheader:
            self.nestedP = True
    def handle_data(self, data):
        if self.inheader and self.nestedP:
            self.headings.append(data)
    def  handle_endtag(self, tag):
        if tag in  ['h1', 'h2', 'h3', 'h4', 'h5',"h6"]:
            self.inheader = False
    def  getHeadings(self):
        return self.headings




def testParser(url):
    from urllib.request import urlopen
    content = urlopen(url).read().decode()
    parser = HeaderParser()
    parser.feed(content)
    return parser.getHeadings()


code.interact(local=dict(globals(), **locals()))