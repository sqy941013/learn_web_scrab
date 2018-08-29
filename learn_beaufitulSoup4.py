from bs4 import BeautifulSoup
import requests


my_proxies={"http":"http://127.0.0.1:1080","https":"https://127.0.0.1:1080"}
url = 'https://www.youtube.com/channel/UCkJjLkIZiQ708cOg_SBUU6A/videos'

response = requests.get(url,proxies=my_proxies,timeout=5)
html_str = response.text
#print response.content

soup = BeautifulSoup(html_str, 'lxml', from_encoding='utf-8')

# print soup.prettify()
#print soup.title.string
'''
for string in soup.stripped_strings:
    print repr(string)
'''
# print soup.find_all(class_='yt-thumb-clip')
for item_ in soup.find_all(class_='yt-thumb-clip'):
    print item_



