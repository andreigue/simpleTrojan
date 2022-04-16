Writing a simple program with hidden malicious code in the background, scraping victim's folders and sending information back to the main computer.


https://user-images.githubusercontent.com/25357733/163692127-252d2470-ddeb-4057-9c78-bdf7547098f3.mp4

Youtube link: https://www.youtube.com/watch?v=ShEX6RL_HXA

### Malware Subsections:

- scrape victim's files and folders (Desktop/Documents/Downloads), and look for files with the word "bank" in it. If however we find a folder with the word "bank" in it, then we check all files within the folder, regarless of naming.
- Send file to attacker's computer. If file is password protected, unencrypt it first, save in new file, and send that unencrpyted file.

### How to Install

- Clone the repo
- (OPTIONAL) Generate a virtual environment by running `python -m venv env` (or using an IDE) and activate it by running `env\Scripts\activate.bat` (for Windows)
- Install the required packages with `pip install -r requirements.txt`
**Note:** On Windows, if you are having issues with creating a virtual environment due to the Python path, you can fix this by simply going into the Microsoft Store app, and installing Python from there.

### How to Build (on Windows)

- This is to build the client side of the application that the victim would run on their computer. The server is not a part of this build as it is ran sepreatly on the attacker's computer.
- Install pyinstaller (`pip install pyinstaller`)
- Build the app using this command (`pyinstaller --onefile --windowed main.py`)
  - `onefile`: makes a one-file executuble
  - `windowed`: hides the command line window

### Third Party Tools Used

- **[ngrok](https://ngrok.com/)**: Used for TCP Tunneling from ngrok cloud server to the local server.
- **[John the Ripper](https://www.openwall.com/john/)**: Password cracking utility.
- **[office2john](https://github.com/openwall/john/blob/bleeding-jumbo/run/office2john.py)**: Used to get the encrypted password of a password protected Microsoft Word file.
- **[Weakpass](https://weakpass.com/)**: Resource for common password lists.
- **[Aspose.Words](https://github.com/aspose-words/Aspose.Words-for-Python-via-.NET)**: Used to open encrypted document with its password, and save it unecyrpted.
- **[Requests-HTML](https://docs.python-requests.org/projects/requests-html/en/latest/)**: Used to load websites dynamically. This ensures that the webpage loads its scripts, which may cause more images to load on the page.
