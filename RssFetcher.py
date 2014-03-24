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
            
            items.append(Article(title, category, link, description, video_id, alias))

        return items
      
      
    #------------- Get video ID -------------


    def get_video_id(self, page_url):
        page_html = utils.url_request(page_url)
        page_html = page_html.decode()

        #"http://www.youtube.com/embed/p1JuU4OJ9NY"
        m = re.search(r'http://www.youtube.com/embed/(.*)(\" )+', page_html)
        embed_url = m.group()
        
        video_id = embed_url[29:40]
        #print('video_id = ' + video_id)

        return video_id


    #----------------------------------------
    #--------- Get article category ---------


    def get_article_category(self, page_url):
        page_html = utils.url_request(page_url)
        page_html = page_html.decode()
        
        #<a class="c20a blueh" href="/video/index?cat_alias=actual">Actual</a>
        #<a class="c20a blueh" href="/video/index?cat_alias=predici">Predici</a>
        #<a class="c20a blueh" href="/video/index?category=546">Romani II</a>
        #<a class="c20a greenh" href="/news/index?cat_alias=nationale">Naționale</a>
        #<a class="c20a blueh" href="/video/index?category=546">Romani II</a>        
        m = re.search(r'<a class=\"c20a\b[^>]*>(.*?)</a>', page_html)
        print(m.group())
        #print(m.group(1))        
        return m.group(1)


    #----------------------------------------
