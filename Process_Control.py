from onshape_client.client import Client
import json

class Process_Control:

    def __init__(self):
        self.initializeClient()
        self.onStartup()




    def initializeClient(self):
    # ----------------------------------------------
    #
    # Handles all of the intialization and settings for the OnshapeAPI
    # Establishes the correct headers, queries, and authorization keys
    #
    # -----------------------------------------------
        self.key = ""
        self.secret = ""
        with open("api-key", "r") as f:
            self.key = f.readline().rstrip()
            self.secret = f.readline().rstrip()
        self.base_url = 'https://cad.onshape.com'

        # Defining accepted headers for requests
        self.headers = {'Accept': 'application/vnd.onshape.v1+json', 'Content-Type':'application/json'}

        # Defining the query parameters of the API requests
        self.query_params = {}
        self.sharedQ = {
           'filter': 2
        }
        # Initializes the client class
        self.client = Client(configuration={"base__url": self.base_url, "access_key": self.key, "secret_key": self.secret})




    def onStartup(self):
    # ----------------------------------------------
    #
    # Handles all of the intialization and settings for the OnshapeAPI
    # Establishes the correct headers, queries, and authorization keys
    #
    # -----------------------------------------------
        self.sharedDocs = {}
        self.keys = []
        self.getAllSharedDocs()




    def getAllSharedDocs(self):
    # ----------------------------------------------
    # Gets all shared documents on the user's account, stores in a dictionary
    # 
    #  KEY: document name on Onshape
    #  VALUE: list of document parameters (did, vid, version description, version name, creator)
    #
    # -----------------------------------------------
        r = self.client.api_client.request('GET', url = self.base_url + '/api/documents', query_params=self.sharedQ, headers = self.headers)
        x = json.loads(r.data)
        for i in range(0,len(x['items'])):
            properties = self.getDocumentProperties(i,x)
            self.keys.append(str(x['items'][i]['name']))
            self.sharedDocs[str(x['items'][i]['name'])] = properties
        return self.keys, self.sharedDocs




    def getDocumentProperties(self, i, x):
    # --------------------------------------------
    # Gets all document properties needed for operation and characterization
    # --------------------------------------------
        properties = []
        properties.append(str(x['items'][i]['id']))
        properties.append(str(self.getVersionID(str(x['items'][i]['id']))))
        description, name, creator = self.getVersionProperties(str(x['items'][i]['id']), str(self.getVersionID(str(x['items'][i]['id']))))
        properties.append(description)
        properties.append(name)
        properties.append(creator)
        return properties




    def getVersionID(self,did):
    # --------------------------------------------
    # Gets the latest versionID of the document in question 
    # --------------------------------------------
        r = self.client.api_client.request('GET', url = self.base_url + '/api/documents/d/' + did +'/versions/', query_params=self.query_params, headers = self.headers)
        x = json.loads(r.data)
        vid = x[len(x)-1]['id']
        return vid




    def getVersionProperties(self,did, vid):
        ## Get the latest document version properties
        r = self.client.api_client.request('GET', url = self.base_url + '/api/documents/d/' + did +'/versions/'+ vid , query_params= self.query_params, headers = self.headers)
        x = json.loads(r.data)
        description = (x['description'])
        name = x['name']
        creator = x["creator"]["name"]
        return description,name, creator




    def formatJSON(self):
        result = {
            "project_name": self.documentName,
            "course": 'ME134',
            "author_name": self.creator.lower(),
            "description": self.description,
            "status": self.name.lower(), 
        }
        print(result)



    def pushVersion(self, name, description):
        query_params={
            "documentId" : str(self.did),
            "name": str(name),
            "description": str(description)
        }
        print(query_params)
        r = self.client.api_client.request('POST', url = self.base_url + '/api/documents/d/' + self.did +'/versions/', query_params={},  body=query_params, headers = self.headers)




    def add_2_processing(self):
        self.pushVersion('PROCESSING','We are currently working on your part request! We will reach out to your team if we have any questions')



    def add_2_completed(self):
        self.pushVersion('COMPLETED', 'Your parts have been completed and are ready for pickup in the dropbox.')



