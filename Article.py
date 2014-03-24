__author__ = 'DAi'

import re


class Article:
    title = ''
    link = ''
    description = ''
    category = ''
    video_id = ''


    def __get_title(self, title):
        #TODO: implement title constructor
        return title            

    def __init__(self, title, category, link, description, video_id, feed_alias):
        self.title = self.__get_title(title)
        self.link = link
        self.description = description
        self.feed_alias = feed_alias
        self.category = category
        self.video_id = video_id

    def __str__(self):
        return '%s - %s' % (self.video_id, self.title)