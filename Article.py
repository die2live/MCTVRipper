__author__ = 'DAi'

import re


class Article:	          

    def __init__(self, title, category, link, description, video_id, feed_alias):
        self.title = title
        self.link = link
        self.description = description
        self.feed_alias = feed_alias
        self.category = category
        self.video_id = video_id
        self.media_url = ''

    def __str__(self):
        return '%s - %s' % (self.video_id, self.title)
