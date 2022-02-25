import os
import sys
from misc.office2john import process_file

FILES_DIR = os.path.join(os.path.dirname(__file__), "./files/")
MISC_DIR = os.path.join(os.path.dirname(__file__), "./misc/")

def isEncryptedDoc(fileName):
    # check is doc
    if not (os.path.splitext(fileName)[1] == ".docx" or os.path.splitext(fileName)[1] == ".doc"):
        return False
    # if doc, check has password
    with open(os.path.join(FILES_DIR, fileName), "rb") as doc:
        return "encryptedVerifierHashInput" in str(doc.read())

# filter to files with passwords
encryptedDocFilesList = [os.path.join(FILES_DIR, f) for f in os.listdir(FILES_DIR) if isEncryptedDoc(f)]

# save passowrd hashes to a file
sys.stdout = open(os.path.join(MISC_DIR, "hash.txt"), "w")
for doc in encryptedDocFilesList:
    process_file(doc)
sys.stdout = sys.__stdout__

# TODO: Use John the ripper to decrypt the passwords