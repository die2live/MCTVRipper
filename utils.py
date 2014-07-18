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
		print('Uploading to FTP %s ...' % filename)
		file = open(filename, 'rb')
		
		ftp.login(ftp_user, ftp_password)		
		
		create_path_if_not_exists(ftp, store_path)
		
		ftp.storbinary('STOR %s' % os.path.join(store_path, file.name), file)
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
	ftp.cwd('~')
	
def get_webfriendly_string(s):
	ret = unidecode(s)
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
	ret = ret.replace(':', '')
	
#----------------------------------------
