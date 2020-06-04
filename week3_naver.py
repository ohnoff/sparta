import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

# client가 robo와 같은 역할(mongodb에 연결)
client = MongoClient('localhost', 27017)
# 새로운 데이터베이스 추가
# dbsparta라는 이름의 데이터베이스가 있으면 가져오고 없으면 추가(get or create)
db = client.dbsparta

# mongodb 추가하기
# db.users.insert_one({'name': 'bobby', 'age': 21})

# mongodb 가져오기
users = list(db.users.find())  # users는 리스트
# age 값이 21인 오브젝트만 가져오기
users = list(db.users.find({'age': 21}))

for user in users:
    print(user['name'])

# 특정한 오브젝트 하나만 찾아보기
# 뒷부분의 , {'_id': False} 부분은 되도록 함께 쓰는 것이 좋다
user = db.users.find_one({'name': 'bobby'}, {'_id': False})


# 크롤링 하고 싶은 사이트 URL
target_url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303'

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(target_url, headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# print(soup)

# $('#cards-box') jquery를 이용해 특정 html 태그의 정보를 가져옴
# .class, #cards-box, div > h1 -> CSS 선택자(셀렉터)
# soup 변수는 jquery와 비슷하게 특정 html 태그의 정보를 가져올 수 있도록 준비된 상태
# bs4 프로그램(BeautifulSoup)이 requests로 받아온 html을 분석해놓음 -> soup
# soup 역시 CSS 선택자를 이용해 정보를 가져올 수 있다

# 선택자 정보 - #old_content > table > tbody > tr > td.title > div > a

# select() 여러 개를 가져온다(for 문에서 사용 가능)
movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:  # 여러 개의 tr 태그를 순서대로 순회
    # select_one 하나를 찾을 때 쓴다(없으면 None 값을 리턴)
    # 만약 여러개가 있다면... 가장 첫 번째를 리턴(이렇게는 사용하지 않는게 좋음)
    a_tag = movie.select_one('td.title > div > a')

    # (변수명) is None : 만약 없다면
    # (변수명) is not None : 만약 있다면
    if a_tag is not None:
        point = movie.select_one('td.point')
        rank = movie.select_one('td.ac > img')

        rank_text = rank['alt']  # 태그 속성은 딕셔너리처럼 가져오면 ok
        a_text = a_tag.text  # 태그의 값을 가져옴 <a>(값)</a>
        point_text = point.text

        # 숫자를 문자열로 str()
        # 문자열을 숫자로 int(), 숫자가 아닌 문자는 에러!
        
        print(int(rank_text), a_text, point_text)
        document = {
            'rank': int(rank_text),
            'title': a_text,
            'point': point_text,
        }
        # db.users.insert_one(document)