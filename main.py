from mailbox import MH
from flask import Flask, request, jsonify
from mHTMLclass import mHTMLclass
from mCustomText import mCustomText
import webbrowser

app = Flask(__name__)

@app.route('/', methods=['GET'])
def userTesting():
    # open in new tab
    new = 2
    # create HTML File using documentation
    mIndex = """
    %s 
    %s 
    %s 
    %s 
    %s 
    %s 
    %s 
    %s 
    %s 
    %s 
    %s 
    %s 
    %s 
    %s
    %s

    
    """ % (mHTMLclass.mDocType, 
    mHTMLclass.mOpenHTML, 
    mHTMLclass.mOpenHead, 
    mHTMLclass.mMeta, 
    mHTMLclass.mLinkCSS,
    mHTMLclass.mOpenTitle, 
    mCustomText.mTitle, 
    mHTMLclass.mCloseTitle, 
    mHTMLclass.mOpenBody,
    mHTMLclass.mOpenHeadings1, 
    mCustomText.mHelloWorldText, 
    mHTMLclass.mCloseHeadings1,
    mHTMLclass.mLinkJS, 
    mHTMLclass.mCloseBody, 
    mHTMLclass.mCloseHTML)

    f = open("index.html", 'a')
    f.write(mIndex)
    f.close()
    url = "index.html"
    webbrowser.open(url,new)

    return '200'
