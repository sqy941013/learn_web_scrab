import requests

url = 'https://www.youtube.com/channel/UCkJjLkIZiQ708cOg_SBUU6A/videos'

r = requests.get(url)
print r.text
