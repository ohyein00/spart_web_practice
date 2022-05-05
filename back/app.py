# coding=utf-8

#flask,pymongo,dnspython,requests,bs4 패키지 설치

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.lrtcs.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/mars", methods=["POST"])
def web_mars_post():
    name = request.form['name']
    address = request.form['address']
    size = request.form['size']
    order = {
        'name': name,
        'address': address,
        'size': size,
    }
    db.mars.insert_one(order)
    return jsonify({
        'name': name,
        'address': address,
        'size': size,
    })

@app.route("/mars", methods=["GET"])
def web_mars_get():
    order_list = list(db.mars.find({},{'_id':False}))
    return jsonify({'data':order_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
