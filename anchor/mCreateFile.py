class mCreateFile:

    def __init__(self, filename, file):
        self.filename = filename
        self.file = file

        createFile(self.filename, self.file)

def createFile(filename, file):
    f = open("%s" %filename, 'w')
    f.write(file)
    f.close()