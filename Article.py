__author__ = 'DAi'


class Article:
    title = ""
    link = ""
    description = ""
    category = ""


    def __get_title(self, title):
        #TODO: implement title constructor
        return title

    def __init__(self, title, link, description):
        self.title = self.__get_title(title)
        self.link = link
        self.description = description

    def __str__(self):
        return self.title