
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.lrtcs.mongodb.net/Cluster0?retryWrites=true&w=majority')
app = Flask(__name__)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket = list(db.bucket.find({},{'_id':False}))
    return jsonify({'data': bucket})


@app.route("/bucket", methods=["POST"])
def bucket_post():
    content = request.form['bucket']
    num = 0
    for bucketItem in db.bucket.find().sort('id',-1).limit(1):
        num = bucketItem['id'] +1
    bucket = {
        'id': num,
        'bucket': content,
        'complete': 0,
    }
    db.bucket.insert_one(bucket)
    return jsonify({
        'msg': 'POST 완료',
    })


@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    id = int(request.form['id'])
    findBucket = db.bucket.find_one({'id':id})
    if findBucket['complete'] == 0:
        db.bucket.update_one({'id': id}, {'$set': {'complete': 1}})
    else:
        db.bucket.update_one({'id': id}, {'$set': {'complete': 0}})
    return jsonify({'msg': 'POST(완료) 연결 완료!'})


@app.route("/bucket/delete", methods=["POST"])
def bucket_delete():
    id = int(request.form['id'])
    db.bucket.delete_one({'id':id})
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
