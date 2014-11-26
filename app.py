#!venv/bin/python
import json
from flask import Flask, jsonify
from flask import make_response
from difflib import SequenceMatcher
from difflib import Differ
from pprint import pprint
app = Flask(__name__,static_url_path='')


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/getsimilarity/<string:text1>/<string:text2>/', methods=['GET'])
def getdelta(text1,text2):
     s = SequenceMatcher(lambda x: x == " ", text1, text2)
     r=s.ratio()
     latest={}
     latest['ratio']=round(r*100)
     return json.dumps(latest)    



@app.route('/getdelta/<string:text1>/<string:text2>/', methods=['GET'])
def getsimilarity(text1,text2):
       ret={}
       d=Differ()
       t1=text1.splitlines(1)
       t2=text2.splitlines(1)
       result=list(d.compare(t1,t2))
       ret['delta']=result
       return json.dumps((ret))



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)