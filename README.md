# Onshape_Process_Control_FLASK
An exploration in leveraging Onshape as a 3D viewer and File management platform to control and organize Job shop operations.

## How this works 
This code is the basis for communication with the OnshapeAPI in order to push new versions of a document to manage job shop processes. Onshape can upload any file type and view it using it's part studios. This demo allows the user to specify a course to work on and then get all documents that are shared with the user's account that are requesting parts to be made.

## How to use this app
When an engineer finishes their design and is ready to get their parts fabricated, they create a document with the following format as a name 

### COURSE GROUP PROJECT , i.e. ME134 GROUP1 PROJECT 1

In order for the job shop to know that the parts are ready to be made, the users create a version of this document with the version name **QUEUED** and a description that states the quantities of each part to be manufactured. 

Once the 

