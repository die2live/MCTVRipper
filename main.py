import pafy
import urllib.request
import feedparser
from unidecode import unidecode
import re


RSS_URL = "http://moldovacrestina.md/rss/video"
#RSS_URL = "http://feeds.gawker.com/lifehacker/vip"

YOUTUBE_EMBED_URL = "http://www.youtube.com/embed/"

#---------------------------------------
#---------------- UTILS ----------------


def url_request(url):
    """
    Make a url request
    """
    req = urllib.request.urlopen(url)
    return req.read()

#----------------------------------------
#-------------- Fetch RSS ---------------


def get_rss_items(rss_url):
        feed = feedparser.parse(rss_url)

        items = []

        for item in feed['entries']:
            title = unidecode(item['title'])
            link = item['link']
            description = unidecode(item['description'])
            items.append(Article(title, link, description))

        return items


#----------------------------------------
#------------ Download audio ------------


def download_audio(url):
    #url = "http://www.youtube.com/watch?v=I0dQx4SNSwE"
    video = pafy.new(url)
    best = video.getbestaudio("m4a")
    filename = unidecode(video.title)
    best.download(filename)


#----------------------------------------
#------------- Get video ID -------------


def get_video_id(page_url):
    page_html = url_request(page_url)
    page_html = page_html.decode()

    m = re.search(r'http://www.youtube.com/embed/(.*)(\" )+', page_html)
    print(m.group(0))



    #"http://www.youtube.com/embed/p1JuU4OJ9NY"

    #start = index_start_url + 30
    #print(start)

    #video_id = page_html[start, 11]

    #return video_id


#----------------------------------------


def main():
    #get articles from RSS
    rss_articles = get_rss_items(RSS_URL)

    #get HTML contents
    for a in rss_articles:
        print(a)
        video_id = get_video_id(a.link)
        print(video_id)


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