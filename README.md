# Onshape_Process_Control_FLASK
An exploration in leveraging Onshape as a 3D viewer and File management platform to control and organize Job shop operations.

## How this works 
This code is the basis for communication with the OnshapeAPI in order to push new versions of a document to manage job shop processes. Onshape can upload any file type and view it using it's part studios. This demo allows the user to specify a course to work on and then get all documents that are shared with the user's account that are requesting parts to be made.

## How to Send Files to the Job Shop
When an engineer finishes their design and is ready to get their parts fabricated, they create a document with the following format as a name 

### COURSE GROUP PROJECT , i.e. ME134 GROUP1 PROJECT 1

In order for the job shop to know that the parts are ready to be made, the users create a version of this document with the version name **QUEUED** and a description that states the quantities of each part to be manufactured. 

## How the App works
This app works now to categorize the process of working on these files by using the following keywords

  ### QUEUED: waiting to start production
  ### PROCESSING: currently being fabricated
  ### COMPLETED: the parts are fabricated and ready for pickup
  
after connecting the REACT front end the job shop will be able to control and log the flow of the parts currently in production. Because the creator and the job shop will be able to see the current version of the document, this will serve as a communication method between the creator and the jobshop.

## How to Run this DEMO
Download this repository and make sure that you have both the onshape-client and flask installed. I recommend creating a virtual environment to test this out in case you have any issues. 

Run the below bash command to set the flask environment variable for this app. 

```bash
export FLASK_APP = main.py
```
After you have set the variable run
```bash
flask run
```
and the server will start up so that you can see your shared documents and access all of the endpoints of this flask app.

## Endpoints

### /sharedDocs
Returns all of the documents shared with the user's account that have the course prefix they are currently working on

### /refresh
Refreshes the sharedDocs list

### /queue/did
Adds the document with user entered did to the queued state, by updating the version

### /processing/did
Adds the document with user entered did to the processing state, by updating the version

### /completed/did
Adds the document with user entered did to the completed state, by updating the version

### Questions?
If you have any questions about running this demo, shoot me an email @ o.s.gervais@gmail.com 
