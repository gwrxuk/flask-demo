from flask import Flask, send_from_directory, json, g, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from api.HelloApiHandler import HelloApiHandler
from flask_mysqldb import MySQL


app = Flask(__name__, static_url_path='', static_folder='../frontend/build')
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSOWRD"]="0000"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_DB"] = "demo"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
auth = HTTPTokenAuth(scheme="Bearer")
tokens = {
    'token1':'john',
    'tolken2':'susan'
}
CORS(app)
api = Api(app)
mysql = MySQL()
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
    cs = mysql.connection.cursor()
    #cs.execute('''CREATE TABLE TEST (id INTEGER, name VARCHAR(20))''')
    cs.execute('''INSERT INTO TEST VALUES (1, 'Harry')''')
    cs.execute('''INSERT INTO TEST VALUES (2, 'Arthor')''')
    mysql.connection.commit()
    cs.execute('''SELECT * FROM TEST''')
    Executed_DATA = cs.fetchall()
    print(Executed_DATA)
    return str(Executed_DATA[1]['name'])

@app.route("/api/login", methods={"POST"})
def login():
    j = json.loads(request.data)
    print(j["username"])
    return "token1"


@app.route("/", methods={"GET"})
def index():
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(HelloApiHandler, '/flask/hello')