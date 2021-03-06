from flask import Flask, request
import sqlite3, json
from flask import current_app, g
from flask.cli import with_appcontext
from flask_basicauth import BasicAuth
from logging.config import dictConfig

DATABASE = '/usr/src/app/database.db'

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'requirements'
app.config['BASIC_AUTH_PASSWORD'] = 'engineering'

basic_auth = BasicAuth(app)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def query_db(query, args=()):
    con = get_db()
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    con.commit()
    cur.close()
    return rv

def setup_db():
    query_db('''CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time DATETIME DEFAULT CURRENT_TIMESTAMP,
        data TEXT
        );'''
    )

# App code

@app.route('/api', methods = ['POST'])
def submit():
    data = json.dumps(request.get_json())
    print("DATA {}".format(data))
    query_db('INSERT INTO results(data) VALUES (?)', (data, ))
    return 'OK'

@app.route('/api/dl', methods = ['GET'])
@basic_auth.required
def download():
    res = []
    rows = query_db('SELECT * FROM results')
    for i in rows:
        jsonData = json.loads(i['data'])
        jsonData['_ID'] = i['id']
        jsonData['_TS'] = str(i['time'])
        res.append(jsonData)

    return json.dumps(res)

@app.route('/api/setup', methods = ['GET'])
@basic_auth.required
def setup():
    setup_db()
    return 'OK'
