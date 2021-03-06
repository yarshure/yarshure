"""
httpExists.py
A quick and dirty way to check whether a web file is there.
Usage:
>>> import httpExists
>>> httpExists.httpExists('http://www.python.org/')
True
>>> httpExists.httpExists('http://www.python.org/PenguinOnTheTelly')
Status 404 Not Found : http://www.python.org/PenguinOnTheTelly
False
"""
import httplib, urlparse
import socket
socket.setdefaulttimeout(8.0)

def httpExists(host,url):
#host, path = urlparse.urlsplit(url)[1:3]
    if ':' in host:
        # port specified, try to use it
        host, port = host.split(':', 1)
        try:
            port = int(port)
        except ValueError:
            print 'invalid port number %r' % (port,)
            return False
    else:
        # no port specified, use default port
        port = None
    try:
        if port ==443:
	    method="POST"
	    connection = httplib.HTTPSConnection(host, port=port)
	else:
	    method="HEAD"
            connection = httplib.HTTPConnection(host, port=port)
	connection.request(method, url)

#        connection.request("HEAD", "http://www.segame.com/index.sega")
        resp = connection.getresponse()
        if resp.status == 200:       # normal 'found' status
            found = 200 
#            print "Status %d %s : %s" % (resp.status, resp.reason, url)
#elif resp.status == 302:     # recurse on temporary redirect
#            found = httpExists(urlparse.urljoin(url,
#                               resp.getheader('location', '')))
        else:                        # everything else -> not found
#print "Status %d %s : %s" % (resp.status, resp.reason, url)
            found = resp.status
    except Exception, e:
#print e.__class__, e, url
        found = False
    return found
def _test():
    import doctest, httpExists
    return doctest.testmod(httpExists)
if __name__ == "__main__":
    _test()
