import requests
import bs4
from youtube_dl import YoutubeDL
import json


url = 'https://www.apple.com/itunes/charts/songs/'

response = requests.get(url)

bs = bs4.BeautifulSoup(response.content,'html.parser')

all_a_tag = bs.find('div',id = 'main').find_all('li')
data_crawler = []
print(len(all_a_tag))
for v in all_a_tag:
    post = {}
    post['song'] = v.h3.a.string
    post['link'] = v.h3.a.attrs['href']
    post['artis'] = v.h4.a.string
    data_crawler.append(post)

import pyexcel
pyexcel.save_as(records = data_crawler, dest_file_name = 'iTunstopsongs.xlsx')

options = {
    'default_search': 'ytsearch',
    'max_downloads' : 1,
    'format' : 'bestaudio/audio'
}

for i in data_crawler:
    dl = YoutubeDL(options)
    dl.download([i['song']+i['artis']])
