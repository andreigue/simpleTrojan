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

# Use John the ripper to decrypt the passwords
# by default, using project directory as relative folder 
os.system('cmd /c "server\\misc\\john\\run\\john.exe --wordlist=server\\misc\\Top304Thousand-probable-v2.txt server\\misc\\hash.txt"')
os.system('cmd /c "server\\misc\\john\\run\\john.exe --show server\\misc\\hash.txt > server\\misc\\crackedPasswords.txt"')

docPasswdsDict = {}

with open(os.path.join(MISC_DIR, "crackedPasswords.txt"), "r") as f:
    while True:
        curLine = f.readline().rstrip()
        if not curLine:
            break
        docNamePasswd = curLine.split(":")
        docPasswdsDict[docNamePasswd[0]] = docNamePasswd[1]

        