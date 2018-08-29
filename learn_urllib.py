import urllib2

# GET
url = 'https://www.youtube.com/channel/UCkJjLkIZiQ708cOg_SBUU6A/videos'
# request
request = urllib2.Request(url)
# response
response = urllib2.urlopen(request, timeout=10)
html = response.read()
print html


