import webbrowser
class mWebBrowser:
    def __init__(self, filepath):
        self.filepath = filepath

        webBrowser(self.filepath)

def webBrowser(filepath):
    new = 2  # open in new tab
    url = filepath
    webbrowser.open(url,new)
