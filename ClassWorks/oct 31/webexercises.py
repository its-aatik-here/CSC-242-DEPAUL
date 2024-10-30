from urllib.request import *

def urlFcn(url, word):
    #url="http://facweb.cdm.depaul.edu/asettle/web/test.html"
    #word="paragraph"
    file=urlopen(url)
    html=file.read()
    html = html.decode()
    #print(html)
    print(html.count(word))

def countwords(url, wlst):
    file = urlopen(url)
    html = file.read().decode()
    for word in wlst:
        print(f'{word} appears {html.count(word)} times')
