from bs4 import BeautifulSoup
import requests
import re

my_proxies = {"http": "http://127.0.0.1:1080", "https": "https://127.0.0.1:1080"}
url = 'https://www.youtube.com/channel/UCgIGMDYhCqiwls28cygpYqg/videos'

response = requests.get(url,proxies=my_proxies,timeout=5)
html_str = response.text
#print response.content
soup = BeautifulSoup(html_str, 'html.parser', from_encoding='utf-8')
# print soup.prettify()
#print soup.title.string
'''
for string in soup.stripped_strings:
    print repr(string)
'''
image_list = []
# Regex to match url start with https://
img_url_patten = re.compile(r'^https://(.*?)')
# print soup.find_all(class_='yt-thumb-clip')
for image in soup.find_all(class_='yt-thumb-clip'):
    if re.match(img_url_patten, image.img.get('src')):
        image_list.append(image.img.get('src'))

#for x in image_list:
#    print x

title_list = []
title_patten = re.compile(r'^.*(?=\s-)')
video_link_list = []
for title in soup.find_all(class_='yt-uix-tile-link'):
    #print title.get('title')
    title_list.append(re.findall(title_patten, title.get('title')))
    video_link_list.append(title.get('href'))

for x in title_list:
    print x



