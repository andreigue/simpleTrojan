# gitPractice

Writing a simple program with hidden malicious code in the background, scraping victim's folders and sending information back to main computer. Goal: practice Git commands in a collaborative fashion.

### Malware Subsections:

- scrape victim's files and folders (Desktop/Documents/Downloads), and look for files with the word "bank" in it. If however we find a folder with the word "bank" in it, then we check all files within the folder, regarless of naming.
- Send file to attacker's computer. If file is password protected, unencrypt it first, save in new file, and send that unencrpyted file.

### Things to Practice:

git squash
git revert (go back in commits)
git branch

### How to Install

- Clone the repo
- (OPTIONAL) Generate a virtual environment by running `python -m venv env` (or using an IDE) and activate it by running `env\Scripts\activate.bat` (for Windows)
- Install the required packages with `pip install -r requirements.txt`
**Note:** On Windows, if you are having issues with creating a virtual environment due to the Python path, you can fix this by simply going into the Microsoft Store app, and installing Python from there.

### Third Party Tools Used

- **ngrok (https://ngrok.com/)**: Used for TCP Tunneling from ngrok cloud server to local server
- **John the Ripper (https://www.openwall.com/john/)**: Password cracking utility
- **office2john (https://github.com/openwall/john/blob/bleeding-jumbo/run/office2john.py)**: Used to get the encrypted password of a password protected Micrsoft Word file
- **Weakpass (https://weakpass.com/)**: Resource for common password lists
- **Aspose.Words (https://github.com/aspose-words/Aspose.Words-for-Python-via-.NET)**: Used to open encrypted document with its password, and save it unecyrpted
