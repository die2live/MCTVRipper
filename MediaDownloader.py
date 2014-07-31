# -*- coding: utf-8 -*-
__author__ = 'DAi'

import pafy
from unidecode import unidecode
import utils


class MediaDownloader(object):

    def download_audio(self, url, save_path, title):
        # url = "http://www.youtube.com/watch?v=I0dQx4SNSwE"
        video = pafy.new(url)
        best = video.getbestaudio('m4a')
        
        if best != None:
            filename = save_path + self.__get_filename(title, best.extension)
            best.download(filename)
            return filename
        
        return ''

    def __get_filename(self, title, extension):        
        ret = unidecode(title)
        ret = utils.get_webfriendly_string(ret)
        print ret
        return ret + '.' + extension
