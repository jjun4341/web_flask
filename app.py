from flask import Flask
from gevent.pywsgi import WSGIServer
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
coll = client.shop.user

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"
    
@app.route('/db')
def date():
    return coll.find_one({"item": '테스트'})
if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()