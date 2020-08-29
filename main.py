from flask import Flask
from markupsafe import escape
from Process_Control import Process_Control

app = Flask(__name__)
p_c = Process_Control()

@app.route('/')
def index():
    return 'main page'



#@app.route('/sharedDocs')
#def sharedDocs():
#    docs = p_c.sharedDocs
#    return docs



@app.route('/refreshDocs')
def refreshDocs():
    p_c.getAllSharedDocs()
    docs = p_c.sharedDocs
    return docs


@app.route('/queue/<did>')
def queue(did):
    # show the user profile for that user
    p_c.pushQUEUED(did)
    return 'Pushed version QUEUED for did:%s' % escape(did)



@app.route('/processing/<did>')
def processing(did):
    # show the user profile for that user
    p_c.pushPROCESSING(did)
    return 'Pushed version PROCESSING for did:%s' % escape(did)



@app.route('/completed/<did>')
def completed(did):
    # show the user profile for that user
    p_c.pushCOMPLETED(did)
    return 'Pushed version COMPLETED for did:%s' % escape(did)





