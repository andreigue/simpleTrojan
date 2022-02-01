import os

folders = ["Desktop", "Documents", "Downloads"]    

# TODO: Consider system with multiple drives
folderPathList = [os.path.join(os.environ['USERPROFILE'], x) for x in folders]

# look for "bank" within file/folder names
def getFilesInPath(path):
    fileList = [f for f in os.listdir(path) if "bank" in f.lower()]
    return fileList

for path in folderPathList:
    fileList = getFilesInPath(path)


# test code
# getFilesInPath(os.path.abspath(""))