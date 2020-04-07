from flask import Flask, request,jsonify
from reqs import getRepos, get_with_lang,get_with_limits

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"

@app.route("/repos")
def repoResp():
    queryarg = request.args.get('q')
    languagearg = request.args.get('language')
    limitarg=request.args.get('limit',type=int)
    if queryarg!=None and limitarg != None:
        return jsonify(get_with_limits(queryarg,limitarg)) #jsonify converts the list to json response
    elif queryarg is not None and languagearg is None:
        return getRepos(queryarg)
    elif languagearg != None :
        return get_with_lang(queryarg, languagearg)
    