from flask import Flask, render_template, request, jsonify, make_response
from markupsafe import escape
from Process_Control import Process_Control
from flask_cors import CORS, cross_origin

app = Flask(__name__)
p_c = Process_Control()

CORS(app)


@app.route('/', methods=['OPTIONS'])
def index():
    return 'main page'


@app.route('/refreshDocs')
def refreshDocs():
    return {"docs": p_c.sharedDocs}


@app.route('/pending/<did>')
def pending(did):
    # show the user profile for that user
    p_c.pushPENDING(did)
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
