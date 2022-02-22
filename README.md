# gitPractice
Writing a simple program with hidden malicious code in the background, scraping victim's folders and sending information back to main computer. Goal: practice Git commands in a collaborative fashion.

### malware subsections:
- scrape victim's files and folders (Desktop/Documents/Downloads), and look for files with the word "bank" in it. If however we find a folder with the word "bank" in it, then we check all files within the folder, regarless of naming.
- Send file to attacker's computer. If file is password protected, unencrypt it first, save in new file, and send that unencrpyted file. 

### things to practice:
git squash
git revert (go back in commits)
git branch

### third part tools used
- **ngrok (https://ngrok.com/)**: Used for TCP Tunneling from ngrok cloud server to local server
- **John the Ripper (https://www.openwall.com/john/)**: Password cracking utility
- **office2john (https://github.com/openwall/john/blob/bleeding-jumbo/run/office2john.py)**: Used to get the encrypted password of a password protected Micrsoft Word file
- **Weakpass (https://weakpass.com/)**: Resource for common password lists