# -*- coding: utf-8 -*-
__author__ = 'DAi'

from feedgen.feed import FeedGenerator
from goose import Goose

class PodcastGenerator:    

	def get_feedgenerator(self):
		fg = FeedGenerator()
		fg.id('http://pod.w-me.net')
		fg.title('W-Me Podcast')
		fg.description('W-Me podcast')
		fg.author( {'name':'Alex Dai','email':'pod@w-me.net'} )
		fg.link( href='http://pod.w-me.net', rel='alternate' )
		fg.logo('http://pandodaily.files.wordpress.com/2012/08/shutterstock_58664.jpg')
		#fg.subtitle('This is a cool feed!')
		fg.link( href='http://pod.w-me.net/feed.atom', rel='self' )
		fg.language('en')
		fg.load_extension('podcast')
		fg.podcast.itunes_category('Technology', 'Podcasting')	 
		return fg
		
	def build_rss_file(self, fg):		
		fg.rss_file('./../tmp/podcast.xml') 
		return './../tmp/podcast.xml'
	
	def add_entry(self, fg, item, media_url):
		print('Adding entry for item %s and media %s' % (item.video_id, media_url))
		fe = fg.add_entry()
		## TODO fe.id('http://lernfunk.de/media/654321/1')
		fe.title(item.title)
		fe.content(self.get_entry_content(item.link))
		fe.enclosure(media_url)
		
		##TODO
		
		
	def get_entry_content(self, url):
		g = Goose()
		article = g.extract(url = url)		
		
		#print(article.title)
		#print(article.meta_description)
		#print(article.cleaned_text)
		#print(article.top_image.src)
		#print(article.movies)		
		return article.cleaned_text
		
