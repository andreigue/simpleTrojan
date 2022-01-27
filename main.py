# part 1: Write a benign-looking program, such as image extractor from a website 
#         which the user inputs. Ask to choose a folder within the system using a 
#         pop-up file explorer. 
import tkinter as tk
from tkinter import filedialog as fd

window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()
window.mainloop()


# part 2: When the executable is ran, have Desktop scraper in the background working