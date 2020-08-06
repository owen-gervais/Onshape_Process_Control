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

