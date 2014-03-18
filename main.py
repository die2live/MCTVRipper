import urllib.request
import re

from RssFetcher import RssFetcher
from MediaDownloader import MediaDownloader

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
#------------- Get video ID -------------


def get_video_id(page_url):
    page_html = url_request(page_url)
    page_html = page_html.decode()

    #"http://www.youtube.com/embed/p1JuU4OJ9NY"
    m = re.search(r'http://www.youtube.com/embed/(.*)(\" )+', page_html)

    embed_url = m.group()
    print(embed_url)

    video_id = embed_url[29:40]

    return video_id


#----------------------------------------


def main():
    #get articles from RSS
    rss_articles = RssFetcher.get_rss_items(RSS_URL)

    #get HTML contents
    for a in rss_articles:
        print(a)
        video_id = get_video_id(a.link)
        print(video_id)
        md = MediaDownloader()
        md.download_audio(video_id, 'tmp/', a.title)


if __name__ == '__main__':
    main()