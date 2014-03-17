import sys

sys.path.append(r"/home/code4him/local/lib/python2.6/site-packages")
import pafy
from unidecode import unidecode
import urllib.request
#import simplejson as json
import feedparser
#from xml2json import xml2json

RSS_URL = "http://moldovacrestina.md/rss/video"
#RSS_URL = "http://feeds.gawker.com/lifehacker/vip"


def download_audio(url):
    #url = "http://www.youtube.com/watch?v=I0dQx4SNSwE"
    video = pafy.new(url)
    best = video.getbestaudio("m4a")
    fileName = unidecode(video.title)
    best.download(fileName)


def get_rss_content(rss_url):
    return get_json(rss_url)


def get_mctv_article_links(rssjson):
    links = []
    for article in rssjson:
        #links.append(article[0]["link"])
        print(article)
    return links


#---------------------------------------

def get
    _rss_items(rss_url):
    feed = feedparser.parse(rss_url)

    items = []

    for item in feed['entries']:
        title = unidecode(item['title'])
        link = item['link']
        description = unidecode(item['description'])
        items.append(Article(title, link, description))

    return items


#def get_json(url):
#    """
#    Make a url request and return as a JSON object
#    """
#    res = urlrequest(url)
    #decodedres = unidecode(res)
    #return loads(res)
    #obj = objectify.fromstring(decodedres)
    #json = objectJSONEncoder().encode(obj)
#    options = type("OptionParser", (object,), {"pretty": False})
    #jsonfromxml = xml2json(res, options)
    #return jsonfromxml  #json.load(jsonfromxml)


def urlrequest(url):
    """
    Make a url request
    """
    req = urllib.request.urlopen(url)
    return req.read()


#----------------------------------------

def main():
    #rss_content = get_rss_content(RSS_URL)
    article_links = get_rss_items(RSS_URL)
    for a in article_links:
        print(a)


class Article:
    title = ""
    link = ""
    description = ""

    def __init__(self, title, link, description):
        self.title = title
        self.link = link
        self.description = description

    def __str__(self):
        return self.title


if __name__ == '__main__':
    main()