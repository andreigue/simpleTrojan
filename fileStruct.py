import os
from turtle import down

folders = ["Desktop", "Documents", "Downloads"]    

folder_list = [os.path.join(os.environ['USERPROFILE'], x) for x in folders]

# look for "bank" within file/folder names