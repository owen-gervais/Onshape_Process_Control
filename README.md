# Onshape_Process_Control
An exploration in leveraging Onshape as a 3D viewer and File management platform to control and organize Job shop operations.


## GET Shared Documents:

### url 
= /api/documents,
### query_params 
={'filter':2, 'q': "ENTER CLASS NAME HERE"}

Returns all of the shared documents to the user's Onshape Account, you can then parse for the individual document IDs

## Document ID's and Names would be displayed on Front End

Need to make sure to **GET** current version and check if it is **PENDING** for completion. 

Only populate **PENDING** documents

In the Description of the version you will be able to see the parts that need to be manufactured.

## GET Versions:
Solely need the document ID that comes from the **GET** shared Documents to get the most recent version id from the result

## GET Version:
You can just put in the achieved version ID in order to get the version description and state.

## Create Version: 
Updated on Drag to the current state of production and upon entering the final state updated the version and description of the document to teel the user that the prints are ready to be picked up. 
