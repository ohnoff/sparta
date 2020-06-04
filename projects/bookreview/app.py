from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    #ajax에서 가져온 데이터 변수에 저장
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']
    
    #mongodb에 저장할 데이터(오브젝트/도큐먼트)
    review = {

        'title' : title_receive,
        'author' : author_receive,
        'review' : review_receive,
    }

    #dbsparta 데이터베이스의 reviews 콜렉션에 review 도큐먼트 저장
    db.reviews.insert_one(review)

    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    reviews = list( #mongodb 의 결과들(도큐먼트들)을 리스트로 변환
        # {}- 검색조건 (비어있으니 모두 다 가져옴)
        # {'_id' : 0} - _id 정보는 필요없으니 가져오지 않겠다.
        db.reviews.find({}, {'_id': 0})
    )
    return jsonify({'result':'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)