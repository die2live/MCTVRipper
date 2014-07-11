# import urllib.request ###used in python 3.x
import urllib2

#---------------- UTILS ----------------


def url_request(url):
    """
    Make a url request
    """
    # req = urllib.request.urlopen(url) ###used in python 3.x
    req = urllib2.urlopen(url)
    return req.read()


#----------------------------------------