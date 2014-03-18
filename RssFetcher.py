__author__ = 'DAi'

from Article import Article
import feedparser
from unidecode import unidecode


class RssFetcher(object):

    @staticmethod
    def get_rss_items(rss_url):
        feed = feedparser.parse(rss_url)

        items = []

        for item in feed['entries']:
            title = unidecode(item['title'])
            # title = item['title'].decode()
            link = item['link']
            description = unidecode(item['description'])
            # description = item['description'].decode()
            items.append(Article(title, link, description))

        return items
