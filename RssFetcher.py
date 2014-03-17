__author__ = 'DAi'

import feedparser
from unidecode import unidecode


class RssFetcher:
    rss_url = ""

    def __init__(self, rss_url):
        self.rss_url = rss_url

    def get_rss_items(rss_url):
        feed = feedparser.parse(rss_url)

        items = []

        for item in feed['entries']:
            title = unidecode(item['title'])
            link = item['link']
            description = unidecode(item['description'])
            items.append(Article(title, link, description))

        return items
