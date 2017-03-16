import os

from flask import Flask
from flask import Flask, render_template, jsonify
from flask import Flask, render_template, request
from flask import request
from imdbpie import Imdb


app = Flask(__name__)
@app.route('/api1', methods=['GET'])
def api1():
    print "Hello I am in api1"
    #imdb = Imdb()
    imdb = Imdb(anonymize=True)
    print imdb
    print type(imdb)
    var1 = imdb.top_250()
    print var1
    """var2 = imdb.search_for_title("FightClub")
    print var2
    #req = request.var1"""
    return jsonify(var1)
    return render_template('index.html')

@app.route('/', methods=['GET'])
def index():
    print "Hello I am in index"
    return render_template('index.html')
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)