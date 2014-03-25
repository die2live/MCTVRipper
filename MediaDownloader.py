__author__ = 'DAi'

import pafy
from unidecode import unidecode


class MediaDownloader(object):

    def download_audio(self, url, save_path, title):
        # url = "http://www.youtube.com/watch?v=I0dQx4SNSwE"
        video = pafy.new(url)
        best = video.getbestaudio("m4a")
        best.download(save_path + self.__get_filename(title, best.extension))

    def __get_filename(self, title, extension):        
        ret = unidecode(title)
        ret = ret.lower()
        ret = ret.replace(' ', '_')  
        ret = ret.replace('&quot;', '')  
        ret = ret.replace('&icirc;', 'i')
        ret = ret.replace('&acirc;', 'a')
        ret = ret.replace('_(video)', '')  
        ret = ret.replace(',', '')
        ret = ret.replace('.', '')
        ret = ret.replace('!', '')
        ret = ret.replace('?', '')
        return ret + '.' + extension