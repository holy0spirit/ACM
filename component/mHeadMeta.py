from model.mHTMLclass import mHTMLclass
class mHeadMeta:
    def __init__(self, mTitle):
        self.title = mTitle
    def __str__(self):
        return mMeta(self.title)


def mMeta(mTitle):
    mHead = """
    %s %s %s %s %s %s %s %s
        
    """ % (mHTMLclass.mDocType, 
    mHTMLclass.mOpenHTML, 
    mHTMLclass.mOpenHead, 
    mHTMLclass.mMeta, 
    mHTMLclass.mLinkCSS,
    mHTMLclass.mOpenTitle, 
    mTitle, 
    mHTMLclass.mCloseTitle,)

    return mHead