from onshape_client.client import Client
import json


class Process_Control:
    """ Process Control for Onshape

        This app acts as the base for the Flask backend for the demo job shop process control
        work utilizing the version system to track 

    """

    def __init__(self):
        self.initializeClient()
        self.onStartup()

    def initializeClient(self):
        """ Initializes all of the onshape info for API communication
        """
        self.key = ""
        self.secret = ""
        with open("api-key", "r") as f:
            self.key = f.readline().rstrip()
            self.secret = f.readline().rstrip()
        self.base_url = 'https://cad.onshape.com'

        self.headers = {'Accept': 'application/vnd.onshape.v1+json',
                        'Content-Type': 'application/json'}
        self.currentCourse = 'ME134'
        self.query_params = {}
        self.sharedQ = {
            'filter': 2,
            'q': self.currentCourse
        }
        self.client = Client(configuration={
                             "base__url": self.base_url, "access_key": self.key, "secret_key": self.secret})

    def onStartup(self):
        """ Establishes the functions to run on startup
        """
        self.sharedDocs = []
        self.getAllSharedDocs()

    def formatInfo(self, project_name, pushed_by, description, status):
        """ Formats the json info tag for the box front end

            INPUT: project_name (name of the project, "Course Group")
                   pushed_by    (the name of the user who pushed the latest version)
                   description  (part request of the document user)
                   status       (status of the document working)

            OUTPUT: info (information in the correct format for the front end)

        """
        info = {
            'project_name': project_name,
            'course': self.currentCourse,
            'pushed_by': status,
            'description': pushed_by,
            'status': description
        }
        return info

    def formatProjects(self, info, did, vid):
        """ formats the project info into the json string

            INPUT: info (json object for the front end boxes)
                   did  (document identifier)
                   vid  (version identifier)

            OUTPUT: project (full data of the project)

        """
        project = {
            'info': info,
            'did': str(did),
            'vid': str(vid)
        }
        return project

    def getDocumentProperties(self, i, x):
        """ Gets all shared documents matching the query on the user's account

            INPUT: i (index of interest)
                   x (json object of document values )

            OUTPUT: project_name (name of the project, "Course Group")
                    did          (document identifier)
                    vid          (version identifier)
                    description  (part request of the document user)
                    status       (status of the document working)
                    pushed_by    (the name of the user who pushed the latest version)

        """
        project_name = str(x['items'][i]['name'])
        did = str(x['items'][i]['id'])
        vid = str(self.getVersionID(str(x['items'][i]['id'])))
        description, status, pushed_by = self.getVersionProperties(
            str(x['items'][i]['id']), str(self.getVersionID(str(x['items'][i]['id']))))
        return project_name, did, vid, description, status, pushed_by

    def getVersionID(self, did):
        """ Gets the version ID of the document specified by the did (document identifier)

            INPUT: did (document identifier)

            OUTPUT: vid (version identifier)

        """
        r = self.client.api_client.request('GET', url=self.base_url + '/api/documents/d/' +
                                           did + '/versions/', query_params=self.query_params, headers=self.headers)
        x = json.loads(r.data)
        vid = x[len(x)-1]['id']
        return vid

    def getVersionProperties(self, did, vid):
        """ Gets the version properties of the document specified by the document and version identifiers

            INPUT: did (document identifier)
                   vid (version identifier)

            OUTPUT: description (the request body by the person who pushed the version)
                    status      (current working status of the project)
                    pushed_by   (the user who pushed the latest version, mainly for contact if issues arise)

        """
        r = self.client.api_client.request('GET', url=self.base_url + '/api/documents/d/' +
                                           did + '/versions/' + vid, query_params=self.query_params, headers=self.headers)
        x = json.loads(r.data)
        description = x['description']
        status = x['name']
        pushed_by = x["creator"]["name"]
        return description, status, pushed_by

    def getAllSharedDocs(self):
        """ Gets all shared documents matching the query on the user's account

            INPUT: NONE

            OUTPUT: NONE (Populates the sharedDocs list with all of the matching documents)

        """
        self.sharedDocs = []
        r = self.client.api_client.request(
            'GET', url=self.base_url + '/api/documents', query_params=self.sharedQ, headers=self.headers)
        x = json.loads(r.data)
        for i in range(0, len(x['items'])):
            project_name, did, vid, pushed_by, description, status = self.getDocumentProperties(
                i, x)
            info = self.formatInfo(
                project_name, pushed_by, description, status)
            project = self.formatProjects(info, did, vid)
            self.sharedDocs.append(project)

    def pushVersion(self, status, did):
        """ Pushes an Onshape document version with the name specified by the status variable

            INPUT: status (name of the version)
                   did    (document identifer to update)

            OUTPUT: NONE (POSTs to the OnshapeAPI to update the version of the specified document)

        """
        version_params = {
            "documentId": str(did),
            "name": str(status)
        }
        self.client.api_client.request('POST', url=self.base_url + '/api/documents/d/' +
                                       did + '/versions/', query_params={},  body=version_params, headers=self.headers)

    def pushPENDING(self, did):
        """ Pushes the 'PENDING' version to the specified did 

            INPUT: did (document identifier to update)

            OUTPUT: NONE (calls the pushVersion() method with 'PENDING' status)

        """
        self.pushVersion('pending', did)

    def pushPROCESSING(self, did):
        """ Pushes the 'PROCESSING' version to the specified did 

            INPUT: did (document identifier to update)

            OUTPUT: NONE (calls the pushVersion() method with 'PROCESSING' status)

        """
        self.pushVersion('processing', did)

    def pushCOMPLETED(self, did):
        """ Pushes the 'COMPLETED' version to the specified did 

            INPUT: did (document identifier to update)

            OUTPUT: NONE (calls the pushVersion() method with 'COMPLETED' status)

        """
        self.pushVersion('completed', did)
