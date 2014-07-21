# -*- coding: utf-8 -*-
__author__ = 'DAi'

from Article import Article
import feedparser
import utils
from unidecode import unidecode
import re


class RssFetcher(object):
    
    def get_rss_items(self, rss_url, alias = ''):
        feed = feedparser.parse(rss_url)

        items = []

        for item in feed['entries']:
            title = unidecode(item['title'])
            link = item['link']
            description = unidecode(item['description'])
            video_id = self.get_video_id(link)
            category = self.get_article_category(link)
            
            print('RSS title: %s' % title)
            print('RSS description: %s' % description)
            print('RSS category: %s' % category)
            
            items.append(Article(title, category, link, description, video_id, alias))
            
            print('--------------------')
        return items
      

    #------------- Get video ID -------------


    def get_video_id(self, page_url):
        page_html = utils.url_request(page_url)
        page_html = page_html.decode('utf-8')

        # "http://www.youtube.com/embed/p1JuU4OJ9NY"
        m = re.search(r'http://www.youtube.com/embed/(.*)(\" )+', page_html)
        embed_url = m.group()
        
        video_id = embed_url[29:40]       

        return video_id


    #----------------------------------------
    #--------- Get article category ---------


    def get_article_category(self, page_url):
        page_html = utils.url_request(page_url)
        page_html = page_html.decode('utf-8') 
        
        # <a class="c20a blueh" href="/video/index?cat_alias=actual">Actual</a>
        # <a class="c20a blueh" href="/video/index?cat_alias=predici">Predici</a>
        # <a class="c20a blueh" href="/video/index?category=546">Romani II</a>
        # <a class="c20a greenh" href="/news/index?cat_alias=nationale">Nationale</a>
        # <a class="c20a blueh" href="/video/index?category=546">Romani II</a>        
        
        m = re.search(r'<a class=\"c20a\b[^>]*>(.*?)</a>', page_html)
        
        category = m.group(1)
        print(category)                                
        return utils.get_webfriendly_string(category)


    #----------------------------------------
