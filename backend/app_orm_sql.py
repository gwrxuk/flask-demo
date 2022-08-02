from flask import Flask, send_from_directory, json, g, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from api.HelloApiHandler import HelloApiHandler
from flask_sqlalchemy import SQLAlchemy
from .repository import Product


app = Flask(__name__, static_url_path='', static_folder='../frontend/build')
app.config["SQLALCHEMY_TRACK_MODIFICATIONs"]=False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://demo:0000@127.0.0.1:3306/demo"
auth = HTTPTokenAuth(scheme="Bearer")
tokens = {
    'token1':'john',
    'tolken2':'susan'
}
CORS(app)
api = Api(app)
mysql = SQLAlchemy()
mysql.init_app(app)
@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]
    


@app.route("/api/data", defaults={'path':''}, methods={"POST"})
@auth.login_required
def fetch_all(path):
    print("path %s"%auth.current_user())
    return send_from_directory(app.static_folder,'index.html')

@app.route("/test", methods={"GET"})
def test_db():
    sql_cmd = """SELECT * FROM TEST"""
    query_data = mysql.engine.execute(sql_cmd).fetchall()
    print(query_data)
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