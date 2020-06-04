# 아래 2줄은 항상 제일 위에 위치

from flask import Flask, render_template , jsonify, request
app = Flask(__name__)


# 가운데 부분이 내가 서버 코드를 작성할 곳
@app.route('/')  # "/" -> URL 주소의 나머지 부분
def home(): # home 이라는 함수 이름은 하나만 존재해야 한다.
    # 요청이 들어왔을 때 처리하는 코드
    print('요청이 들어왔습니다!')
    return render_template('index.html') #return 다음 부분이 내가 응답을 줄 내용

#html 문서가 아니라 json 을 리턴해주기
@app.route('/json') 
def test_json(): # home 이라는 함수 이름은 하나만 존재해야 한다.
    # 요청이 들어왔을 때 처리하는 코드
    sample = {'result': 'sample'}
    return jsonify(sample) #return 다음 부분이 내가 응답을 줄 내용
    

@app.route('/test' , methods=['GET']) #GET 메소드 응답만 받겠다!
def test_get():
    # request에는 요청에 대한 정보가 담겨 있음
    # request.args -> 쿼리스트링 정보가 있음
    # 쿼리스트링이란 www.naver.com/?query=호랑이&name=홍길동
    # ? 기호 이후의 주소가 쿼리스트링
    # 아래 정보가 request.args 에 저장됨 (딕셔너리)
    # query=호랑이&name=홍길동 -> {'query': '호랑이', 'name' : '홍길동'}
    # GET 메소드 - request.args - 쿼리스트링 세트로 작업함
    title_receive= request.args.get('title_give')
    print(title_receive)
    return jsonify({'result': 'success' , 'msg': '이 요청은 GET!'})


@app.route('/test', methods=['POST'])
def test_post():
    # request.form에는 ajax의 data 정보가 담겨있음
    # request.form 역시 딕셔너리
    # POST 메소드 - request.form - ajax data 세트로 작업함
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


# 아래 2줄은 항상 제일 아래에 위치 *****
if __name__ == '__main__':
# 0. 0. 0. 0 -> 모든 IP에게 ㅗ는 요청을 받아주겠슴
# port=5000 -> 5000번 포트에 서버를 등록해서 요청을 받아주겠음
# debug=True -> 무언가 에러가 났을 때 에러 메세지를 그대로 보여줌
   app.run('0.0.0.0', port=5000,debug=True)