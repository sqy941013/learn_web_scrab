import urllib2

url = 'https://www.youtube.com/channel/UCkJjLkIZiQ708cOg_SBUU6A/videos'

proxy = urllib2.ProxyHandler({'http': '127.0.0.1:1080'})
opener = urllib2.build_opener(proxy)

response = opener.open(url, timeout=5)
print response.read()
