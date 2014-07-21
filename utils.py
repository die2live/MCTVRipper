# -*- coding: utf-8 -*-
# import urllib.request ###used in python 3.x
import urllib2
import ftplib
import os

#---------------- UTILS ----------------


def url_request(url):
    """
    Make a url request
    """
    # req = urllib.request.urlopen(url) ###used in python 3.x
    req = urllib2.urlopen(url)
    return req.read()


def ftp_upload(filename, store_path, ftp_host, ftp_port, ftp_user, ftp_password):
	"""
	Upload an file via ftp
	"""
	ftp = ftplib.FTP()
	ftp.connect(ftp_host, ftp_port)
	print ftp.getwelcome()
	
	try:
		file = open(filename, 'rb')		
		print('Uploading to FTP %s ...' % file.name)
		
		ftp.login(ftp_user, ftp_password)		
		
		create_path_if_not_exists(ftp, store_path)
		
		print('Current ftp path %s' % ftp.pwd())
		ftp.storbinary('STOR %s' % os.path.basename(file.name), file)		
		ftp.cwd('~')
		ftp.quit()
		
		file.close()
		
	except Exception, e:
		print('Failed to upload %s to FTP. %s' % (filename, e))


def create_path_if_not_exists(ftp, path):
	path_folders = path.split(os.sep)
	for folder in path_folders:			
		if folder not in ftp.nlst():
			ftp.mkd(folder)
		ftp.cwd(folder)				
	
	
def get_webfriendly_string(s):	
	ret = s.lower()
	ret = ret.replace(' ', '_')  
	ret = ret.replace('&quot;', '')  
	ret = ret.replace('&icirc;', 'i')
	ret = ret.replace('&acirc;', 'a')
	ret = ret.replace('_(video)', '')  
	ret = ret.replace(',', '')
	ret = ret.replace('.', '')
	ret = ret.replace('!', '')
	ret = ret.replace('?', '')
	ret = ret.replace(':', '')
	ret = ret.replace('(', '')
	ret = ret.replace(')', '')
	ret = ret.replace(u'ă', 'a')
	ret = ret.replace(u'â', 'a')
	ret = ret.replace(u'î', 'i')
	ret = ret.replace(u'ș', 's')
	ret = ret.replace(u'ț', 't')	
	return ret
	
#----------------------------------------
