from mHTMLclass import mHTMLclass
class mBodyMeta:
    def __init__(self):
        pass
    def __str__(self):
        return mMeta()


def mMeta():
    mBody = """
    %s %s %s %s
        
    """ % (mHTMLclass.mOpenBody,
    mHTMLclass.mLinkJS, 
    mHTMLclass.mCloseBody, 
    mHTMLclass.mCloseHTML)

    return mBody