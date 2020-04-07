from flask import Flask, request,jsonify
from reqs import getRepos, get_with_lang,get_with_limits

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"

@app.route("/repos")
def repoResp():
    queryarg = request.args.get('q')
    languagearg = request.args.get('lang')
    limitarg=request.args.get('limit',type=int)
    if limitarg==None:
        return jsonify(getRepos(queryarg,lang=languagearg,limit=10))
    return jsonify(getRepos(queryarg,lang=languagearg,limit=limitarg))