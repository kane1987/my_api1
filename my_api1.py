from flask import Flask
import json


app = Flask(__name__)


@app.route('/index')
def index():
    res = {'msg': 'this is api', 'msg_code': 0}
    return json.dumps(res)


app.run(port=9002, debug=True)
