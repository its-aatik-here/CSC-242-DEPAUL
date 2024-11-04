from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

def testParser(url):
    content = urlopen(url).read().decode()
    parser = ListParser()
    parser.feed(content)
    return parser.getItems()

class DataCollector(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.text = ""
    def handle_data(self, data):
        self.text += data
    def getData(self):
        return self.text

class NodeParser(HTMLParser):
    def handle_data(self, data):
        print(data)

class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

class AltPrettyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.indent = 0

    def handle_starttag(self, tag, attrs):
        if tag not in {'br', 'hr', 'img'}:
            print(f"{self.indent*' '}{tag} start")
            self.indent += 4
        else:
            print('{}{} start'.format(self.indent*' ', tag))

    def handle_endtag(self, tag):
        self.indent -= 4
        print('{}{} end'.format(self.indent*' ', tag))

class PrettyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.indent = 0

    def handle_starttag(self, tag, attrs):
        if tag not in {'br', 'p'}:
            print(f'{self.indent*" "}{tag} start')
            self.indent += 4

    def handle_endtag(self, tag):
        if tag not in {'p'}:
            self.indent -= 4
            print(f"{self.indent*' '}{tag} end")

class HeaderParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.insideHeader = False
        self.headings = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.insideHeader = True

    def handle_endtag(self, tag):
        if tag.lower() in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.insideHeader = False

    def handle_data(self, data):
        if self.insideHeader:
            self.headings.append(data.strip())

    def getHeadings(self):
        return self.headings

class ListParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.insideListItem = False
        self.items = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'li':
            self.insideListItem = True

    def handle_endtag(self, tag):
        if tag.lower() == 'li':
            self.insideListItem = False

    def handle_data(self, data):
        if self.insideListItem:
            self.items.append(data.strip())

    def getItems(self):
        return self.items

class Collector(HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':
                        self.links.append(absolute)

    def getLinks(self):
        return self.links
