__author__ = 'DAi'

import re


class Article:
    title = ""
    link = ""
    description = ""
    category = ""


    def __get_title(self, title):
        #TODO: implement title constructor
        return title

    def __get_category(self, title):
        #TODO: implement title constructor
        m = re.search(r'http://www.youtube.com/embed/(.*)(\" )+', title)

        return title

    def __init__(self, title, link, description, feed_alias):
        self.title = self.__get_title(title)
        self.link = link
        self.description = description
        self.feed_alias = feed_alias
        self.category = self.__get_category(title)

    def __str__(self):
        return self.title