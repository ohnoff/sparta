import requests
from bs4 import BeautifulSoup

# 크롤링 하고 싶은 사이트 URL
target_url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(target_url, headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# 여기서부터 크롤링 작업

corona = soup.select('#content > div > div:nth-child(5) > table')

for coronas in corona:
    a_tag = corona.select_one('div:nth-child(5) > table')
    if a_tag is not None:
        sec1 = corona.select_one('thead > tr > td')
        sec2 = corona.select_one('tbody > tr > td')

        sec2_text = sec2['alt']  
        a_text = a_tag.text 
        sec1_text = sec1.text
        
        print(int(sec2_text), a_text, sec1_text)
        document = {
            'sec2': int(sec2_text),
            'title': a_text,
            'sec1': sec1_text,
        }