import os

FILES_FOLDER = "./files/"
FILES_DIR = os.path.join(os.path.dirname(__file__), FILES_FOLDER)

def isEncryptedDoc(fileName):
    # check is doc
    if not (os.path.splitext(fileName)[1] == ".docx" or os.path.splitext(fileName)[1] == ".doc"):
        return False
    # if doc, check has password
    with open(os.path.join(FILES_DIR, fileName), "rb") as doc:
        return "encryptedVerifierHashInput" in str(doc.read())

# filter to files with passwords
encryptedDocFilesList = [f for f in os.listdir(FILES_DIR) if isEncryptedDoc(f)]
print(encryptedDocFilesList)

# TODO: get paswords for the files in encryptedDocFilesList
