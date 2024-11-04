from html.parser import HTMLParser
from urllib.request import urlopen

def testParser(url):
    content = urlopen(url).read().decode()
    parser = MyHTMLParser()
    parser.feed(content)

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Encountered a {tag} start tag with attrs {attrs}")
    def handle_endtag(self, tag):
        print(f"Encountered a {tag} end tag")


