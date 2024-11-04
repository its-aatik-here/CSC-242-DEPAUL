from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin

def testParser(url):
    content = urlopen(url).read().decode()
    parser = Collector(url) # ****
    parser.feed(content)
    return parser.getLinks()

# 1. The relative URLs are incomplete
# 2. We need to accumulate the URLs into a list
# To fix #2, we need a constructor
class Collector(HTMLParser):
    'collect links in a page'

    def __init__(self, url):
        'the constructor'
        HTMLParser.__init__(self)
        self.links = list()
        self.url = url

    # change to build our list
    # use urljoin
    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a':
            for tup in attrs:
                if tup[0].lower() == 'href' and not tup[1].lower().startswith('mailto:'):
                    self.links.append(urljoin(self.url, tup[1]))

    def getLinks(self):
        'return the URLs'
        return self.links

class ListParser(HTMLParser):
    'collect the list items in a page in a list'

    def __init__(self):
        'the constructor'
        HTMLParser.__init__(self)
        self.items = []
        self.go = False

    def handle_starttag(self, tag, attrs):
        'report when a tag is a header'
        if tag.lower() == 'li':
            self.go = True

    def handle_endtag(self, tag):
        'report when a tag is a header'
        if tag.lower() == 'li':
            self.go = False

    def handle_data(self, data):
        'gather the data for headers'
        if self.go: # == True
            self.items.append(data.strip())

    def getItems(self):
        'return the list items'
        return self.items

class HeaderParser(HTMLParser):
    'collect the headings in a page in a list'

    def __init__(self):
        'the constructor'
        HTMLParser.__init__(self)
        self.headings = []
        self.go = False
        self.htags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']

    # change self.go
    def handle_starttag(self, tag, attrs):
        'report when a tag is a header'
        if tag.lower() in self.htags:
            self.go = True

    # change self.go
    def handle_endtag(self, tag):
        'report when a tag is a header'
        if tag.lower() in self.htags:
            self.go = False

    # check self.go
    # append the data into the list
    def handle_data(self, data):
        'gather the data for headers'
        if self.go: # == True
            self.headings.append(data.strip())

    def getHeadings(self):
        'return the headings'
        return self.headings

class DataCollector(HTMLParser):
    'collect the data in a page into a string'

    def __init__(self):
        'the constructor'
        HTMLParser.__init__(self)
        self.contents = ''

    def handle_data(self, data):
        'print the data'
        self.contents += data.strip() + " "

    def getData(self):
        'return the string the parser built'
        return self.contents

class PrettyParser(HTMLParser):
    'print tags in an indented way'

    def __init__(self):
        'the constructor'
        HTMLParser.__init__(self) # ****
        self.indent = 0

    # print the tag using self.indent spaces in front -> start
    # change the indentation -> increase
    def handle_starttag(self, tag, attrs):
        'print starting tags'
        print(f"{self.indent * ' '}{tag} start")
        if tag.lower() not in ['br', 'img']:
            self.indent += 4

    # print the tag using self.indent spaces in front -> end
    # change the indentation -> decrease
    def handle_endtag(self, tag):
        'print ending tags'
        self.indent -= 4
        print(f"{self.indent * ' '}{tag} end")

class DataPrinter(HTMLParser):
    'print the data in a page'

    def handle_data(self, data):
        'print the data'
        print(data)

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Encountered a {tag} start tag with attrs {attrs}")
    def handle_endtag(self, tag):
        print(f"Encountered a {tag} end tag")


