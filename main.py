import tkinter as tk
from tkinter import filedialog
from ASCIIConverter import *
from texts import *

RESOLUTION = "800x800"
DEFAULT_FONT = "Calibri"

app = tk.Tk()
app.geometry(RESOLUTION)
app.resizable(False, False)

def shortConversion():
    filename = filedialog.askopenfilename(initialdir = "./", 
        title = "Select a to convert to ASCII art", 
        filetypes = (("PNG files", "*.png*"), ("JPG files", "*.jpg*")))

    print(filename)


TITLE = tk.Label(app, text=TITLE_TXT, font=(DEFAULT_FONT, 30))
TITLE.pack()

ASCII_SELECTION_SHORT_BUTTON = tk.Button(app, text=ASCII_SHORT_TXT, font=(DEFAULT_FONT, 20), command=shortConversion)
ASCII_SELECTION_SHORT_BUTTON.place(relx=0.09, rely=0.3)

ASCII_SELECTION_LONG_BUTTON = tk.Button(app, text=ASCII_LONG_TXT, font=(DEFAULT_FONT, 20))
ASCII_SELECTION_LONG_BUTTON.place(relx=0.5, rely=0.3)

ASCII_SHORT_INSTR = tk.Label(app, text="")


app.mainloop()