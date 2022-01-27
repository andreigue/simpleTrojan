# part 1: Write a benign-looking program, such as image extractor from a website 
#         which the user inputs. Ask to choose a folder within the system using a 
#         pop-up file explorer. 
import tkinter as tk
from tkinter import filedialog as fd

# window
window = tk.Tk()
window.title("Website Image Extractor")
window.geometry('400x200')


# widgets
#-----

# url textbox
urlLabel = tk.Label(text="Website to extract images from:")
urlLabel.pack()
urlTextbox = tk.Text(window, height = 1, width = 20)
urlTextbox.pack()


# file explorer
# TODO: consider using ligtht grey dialog in textbox to indicate what it's for instead
fileDgLabel = tk.Label(text="Folder to save the images in:")
fileDgLabel.pack()

fileDg = tk.Frame()
fileDgTextbox = tk.Text(fileDg, height=1, width=20)
fileDgTextbox.grid(row=0, column=0)

def onFileDialog():
    chosenDirectory = fd.askdirectory()
    fileDgTextbox.delete("1.0", tk.END)
    fileDgTextbox.insert(tk.INSERT, chosenDirectory)
fileDgBtn = tk.Button(fileDg, text="Browse", command=onFileDialog)
fileDgBtn.grid(row=0, column=1)
fileDg.pack()


# submit button
def onSubmit():
    # TODO: should extract the images and save them to specified file location
    pass

submitBtn = tk.Button(window, text="Submit", command=onSubmit)
submitBtn.pack()

#-----

# loop
window.mainloop()


# part 2: When the executable is ran, have Desktop scraper in the background working