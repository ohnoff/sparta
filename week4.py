# 아래 2줄은 항상 제일 위에 위치

from flask import Flask
app = Flask(__name__)


# 가운데 부분이 내가 서버 코드를 작성할 곳
@app.route('/')  # "/" -> URL 주소의 나머지 부분
def home(): # home 이라는 함수 이름은 하나만 존재해야 한다.
    # 요청이 들어왔을 때 처리하는 코드
    print('요청이 들어왔습니다!')
    return '<h1>This is Home!</h1>' #return 다음 부분이 내가 응답을 줄 내용





# 아래 2줄은 항상 제일 아래에 위치 *****
if __name__ == '__main__':
# 0. 0. 0. 0 -> 모든 IP에게 ㅗ는 요청을 받아주겠슴
# port=5000 -> 5000번 포트에 서버를 등록해서 요청을 받아주겠음
# debug=True -> 무언가 에러가 났을 때 에러 메세지를 그대로 보여줌
   app.run('0.0.0.0',port=5000,debug=True)