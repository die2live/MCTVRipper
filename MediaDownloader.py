__author__ = 'DAi'

import pafy
from unidecode import unidecode


class MediaDownloader(object):

    def download_audio(self, url, save_path, title):
        # url = "http://www.youtube.com/watch?v=I0dQx4SNSwE"
        video = pafy.new(url)
        best = video.getbestaudio("m4a")
        best.download(save_path + self.__get_filename(title) + '.m4a')

    def __get_filename(self, title):
        #TODO: implement file name construction
        title = unidecode(title)
        return title