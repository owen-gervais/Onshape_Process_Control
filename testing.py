from flask import Flask
from Process_Control import Process_Control

app = Flask(__name__)
p_c = Process_Control()

@app.route('/')
def index():
    return 'Index Page'

@app.route('/sharedDocs')
def sharedDocs():
    docs = p_c.sharedDocs
    return '{}\' are all of the documents shared with the main account'.format(docs)

@app.route('/refreshDocs')
def refreshDocs():
    p_c.getAllSharedDocs()
    return 'updated the list of shared documents with the master account!'













