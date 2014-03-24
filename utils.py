import urllib.request

#---------------- UTILS ----------------


def url_request(url):
    """
    Make a url request
    """
    req = urllib.request.urlopen(url)
    return req.read()


#----------------------------------------