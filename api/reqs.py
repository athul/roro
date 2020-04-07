import requests
import json
URL="https://api.github.com/search/repositories?"

def getRepos(query=str):
    """This function uses the GitHub API to check for the specified
    query and returns the json response
    """
    response=requests.get(URL+"q="+query)
    data=response.json()
    return makeJson(data)

def get_with_lang(query=str,lang=str):
    """This function works with the language argument which is passed
    from the query parameters which should be of type string. this function
    adds on a language parameter to the github api call
    """
    response=requests.get(URL+"q="+query+"+language:"+lang)
    data=response.json()
    return makeJson(data)

def get_with_limits(query=str,limit=int):
    """This fuctions takes in a limit argument of type int and checks the response with a 
    list slice with the limit. Just the slicer varies this from the getRepos function. Returns a 
    type=list repsonse
    """
    response=requests.get(URL+"q="+query)
    data=response.json()
    jsonresp=makeJson(data)
    return jsonresp['repos'][:limit]

def makeJson(data):
    """
    This function formats the json response with the specific keys and renames them to 
    the needed ones. This returns the formatted json response. 
    """
    data["items"]=[dict(name=k1["full_name"],url=k1["html_url"],description=k1["description"],language=k1["language"]) for k1 in data["items"]]
    jsonData = json.dumps(data)
    js=json.loads(jsonData)
    js.pop('incomplete_results')
    js.pop('total_count')
    js['repos']=js.pop('items')
    return js