__author__ = 'DAi'


class PodcastGenerator:
    episode = []

    def __init__(self, title, description, feed_alias):
        self.title = self.__get_title(title)
        self.link = link
        self.description = description
        self.feed_alias = feed_alias

    def __str__(self):
        return self.title

    def to_xml(self):
        """<?xml version="1.0" encoding="utf-8"?>
        <PodcastGenerator>
            <episode>
                <titlePG><![CDATA[{0[0].titlePG}]]></titlePG>
                <shortdescPG><![CDATA[{0[0].shortdescPG}]]></shortdescPG>
                <longdescPG><![CDATA[{0[0].longdescPG}]]></longdescPG>
                <imgPG></imgPG>
                <categoriesPG>
                    <category1PG>mctv_-_actual</category1PG>
                    <category2PG></category2PG>
                    <category3PG></category3PG>
                </categoriesPG>
                <keywordsPG>MCTV, Actual, Valeriu Ghiletchi, Preotul Vasile, Vladimir Putin, Crimeea, Ucraina</keywordsPG>
                <explicitPG>no</explicitPG>
                <authorPG>
                    <namePG></namePG>
                    <emailPG></emailPG>
                </authorPG>
            </episode>
        </PodcastGenerator>""".format(self)


class episode:
    titlePG = ""
    shortdescPG = ""
    longdescPG = ""
    imgPG = ""
    categoriesPG = categoriesPG()
    keywordsPG = ""
    explicitPG = False
    authorPG = authorPG()


class categoriesPG:
    category1PG = ""
    category2PG = ""
    category3PG = ""


class authorPG:
    namePG = ""
    emailPG = ""