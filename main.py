from RssFetcher import RssFetcher
from MediaDownloader import MediaDownloader

RSS_URL = "http://moldovacrestina.md/rss/video"
#RSS_URL = "http://feeds.gawker.com/lifehacker/vip"

YOUTUBE_EMBED_URL = "http://www.youtube.com/embed/"

#---------------------------------------


def main():
    #get articles from RSS
    rssfetcher = RssFetcher()
    rss_articles = rssfetcher.get_rss_items(RSS_URL, "MCTV")

    #get HTML contents
    for a in rss_articles:
        print(a)        
        md = MediaDownloader()
        try:
            md.download_audio(a.video_id, 'tmp/', a.title)
        except IOError as e:
            #TODO: add some handling
            print(e)
            


if __name__ == '__main__':
    main()