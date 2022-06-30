import imp
from flask import Flask, request, jsonify
from mCustomText import mCustomText
from mHeadMeta import mHeadMeta
from mBodyMeta import mBodyMeta
from mCreateFile import mCreateFile
from mWebBrowser import mWebBrowser


app = Flask(__name__)

@app.route('/', methods=['GET'])
def Index():
    mHead = mHeadMeta(mCustomText.mTitle)
    mBody = mBodyMeta()
    # create HTML File using documentation
    mIndex = """
    %s %s
    """ % ( mHead, mBody)

    mCreateFile("index.html", mIndex) # create html file
    mWebBrowser("index.html") # launch file in web browser
    return '200'
