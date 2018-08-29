import requests

my_proxies={"http":"http://127.0.0.1:1080","https":"https://127.0.0.1:1080"}

url = 'https://www.youtube.com/channel/UCkJjLkIZiQ708cOg_SBUU6A/videos'

response = requests.get(url,proxies=my_proxies,timeout=5)

print response.content