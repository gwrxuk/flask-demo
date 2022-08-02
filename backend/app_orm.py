from flask import Flask, send_from_directory, json, g, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from api.HelloApiHandler import HelloApiHandler
from repository.database import db_session
from repository.models import User, Stock, HistoryStock, Invoice



app = Flask(__name__, static_url_path='', static_folder='../frontend/build')

auth = HTTPTokenAuth(scheme="Bearer")
tokens = {
    'token1':'john',
    'tolken2':'susan'
}
CORS(app)
api = Api(app)

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]
    

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/api/data", defaults={'path':''}, methods={"POST"})
@auth.login_required
def fetch_all(path):
    print("path %s"%auth.current_user())
    return send_from_directory(app.static_folder,'index.html')

@app.route("/test", methods={"GET"})
def test_db():
    u = Invoice("Aa",1,4.0)
    db_session.add(u)
    db_session.commit()
    t = User.query.all()
    print(t[0].name)
    for c, i in db_session.query(User, Invoice).filter(User.id==Invoice.custid).all():
        print(c.name)
    return "ok"

@app.route("/api/login", methods={"POST"})
def login():
    j = json.loads(request.data)
    print(j["username"])
    return "token1"


@app.route("/", methods={"GET"})
def index():
    return send_from_directory(app.static_folder,'index.html')




api.add_resource(HelloApiHandler, '/flask/hello')