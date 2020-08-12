from onshape_client.client import Client
import json

def getAllSharedDocs(query_params, headers):
    r = client.api_client.request('GET', url = base_url + '/api/documents', query_params=query_params, headers = headers)
    x = json.loads(r.data)
    #print(json.dumps(x, indent = 4))
    print(x['items'][0]['name'])
    documentName = x['items'][0]['name']
    did = x['items'][0]['id']
    print(did)
    return documentName, did

def getVersionID(did, query_params, headers):
## Get the current Version ID
    r = client.api_client.request('GET', url = base_url + '/api/documents/d/' + did +'/versions/', query_params=query_params, headers = headers)
    x = json.loads(r.data)
    vid = x[len(x)-1]['id']
    return vid

def getVersionProperties(did, vid, query_params, headers, documentName):
## Get the latest document version properties
    r = client.api_client.request('GET', url = base_url + '/api/documents/d/' + did +'/versions/'+vid , query_params=query_params, headers = headers)
    x = json.loads(r.data)
    description = (x['description'])
    name = x['name']
    creator = x["creator"]["name"]
    formatJSON(description, name, creator, documentName)

def pushVersion(did, headers):
    query_params={
        "documentId" : str(did),
        "name": "Hello",
        "description": "description"
    }
    print(query_params)
    r = client.api_client.request('POST', url = base_url + '/api/documents/d/' + did +'/versions/', query_params={},  body=query_params, headers = headers)






def formatJSON(description, name, creator, documentName):
    result = {
        "project_name": documentName,
        "course": 'ME134',
        "author_name": creator.lower(),
        "description": description,
        "status": name.lower(), 
    }
    print(result)



key = ""
secret = ""


with open("api-key", "r") as f:
    key = f.readline().rstrip()
    secret = f.readline().rstrip()

base_url = 'https://cad.onshape.com'
headers = {'Accept': 'application/vnd.onshape.v1+json', 'Content-Type':'application/json'}
client = Client(configuration={"base__url": base_url, "access_key": key, "secret_key": secret})

##### Getting all of the shared documents with the Current User
query_params = {
    'filter': 2,
}

documentName, did = getAllSharedDocs(query_params,headers)

query_params = {}

vid = getVersionID(did, query_params, headers)

print('---------------------------------------------------------')

getVersionProperties(did,vid,query_params, headers, documentName)

pushVersion(did,headers)


## Get the current Status of that Version 
