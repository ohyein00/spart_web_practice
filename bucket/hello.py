# coding=utf-8
import requests
import json
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.lrtcs.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
apiUrl = 'http://spartacodingclub.shop/sparta_api/seoulair'
movieUrl = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829'
r = requests.get(apiUrl).json()

r_dumps = json.dumps(r, ensure_ascii=False)
r_dict = json.loads(r_dumps, encoding='utf8')

##### 크롤링

data = requests.get(movieUrl,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
movies = soup.select('#old_content>table>tbody>tr')
for movie in movies:
    a_tag = movie.select_one('td.title>div>a')
    if a_tag is not None :
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text # a 태그 사이의 텍스트를 가져오기
        star = movie.select_one('td.point').text # td 태그 사이의 텍스트를 가져오기
        doc = {
            'rank':rank,
            'title':title,
            'star':star
        }
        db.movies.insert_one(doc)


