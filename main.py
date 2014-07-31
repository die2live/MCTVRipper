# -*- coding: utf-8 -*-
from RssFetcher import RssFetcher
from MediaDownloader import MediaDownloader
from PodcastGenerator import PodcastGenerator
import utils
import os

RSS_URL = "http://moldovacrestina.md/rss/video"
#RSS_URL = "http://feeds.gawker.com/lifehacker/vip"

YOUTUBE_EMBED_URL = "http://www.youtube.com/embed/"

#---------------------------------------


def main():
    #get articles from RSS
    rssfetcher = RssFetcher()
    rss_articles = rssfetcher.get_rss_items(RSS_URL, "MCTV")
    
    print('--------------------')
    print('--------------------')
    print('--------------------')

    podcast = PodcastGenerator()
    fg = podcast.get_feedgenerator()
    
    for a in rss_articles:
        print(a)        
        md = MediaDownloader()
        
        try:
            print('Downloading video with id %s...' % a.video_id)
            filename = md.download_audio(a.video_id, '../tmp/', a.title)
            
            if filename != '':
                store_path = os.path.join('media', a.category)
                utils.ftp_upload(filename, store_path, 'ftp.w-me.net', 21, 'pod@w-me.net', '6NAmo@Jr+u9!')
            
                podcast.add_entry(fg, a, os.path.join(u'http://pod.w-me.net', store_path, os.path.basename(filename)))
            
        except IOError as e:
            #TODO: add some handling
            print(e)
        print('--------------------')
        
    rssfile = podcast.build_rss_file(fg)
    utils.ftp_upload(rssfile, '~', 'ftp.w-me.net', 21, 'pod@w-me.net', '6NAmo@Jr+u9!')

if __name__ == '__main__':
    main()
