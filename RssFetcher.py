__author__ = 'DAi'

from Article import Article
import feedparser
from unidecode import unidecode


class RssFetcher(object):

    @staticmethod
    def get_rss_items(rss_url, alias = ''):
        feed = feedparser.parse(rss_url)

        items = []

        for item in feed['entries']:
            title = unidecode(item['title'])
            link = item['link']
            description = unidecode(item['description'])
            items.append(Article(title, link, description, alias))

        return items
