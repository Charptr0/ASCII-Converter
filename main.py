import tkinter as tk
from tkinter import filedialog
from tkinter.constants import BOTTOM, S
from ASCIIConverter import *
from texts import *
import ntpath

RESOLUTION = "800x800"
DEFAULT_FONT = "Calibri"

app = tk.Tk()
app.geometry(RESOLUTION)
app.resizable(False, False)
app.title(TITLE_TXT)

'''
Open the window for the user to choose an image

Return the image path
'''
def getImagePath():
    filePath = filedialog.askopenfilename(initialdir = "./", 
        title = "Select a to convert to ASCII art", 
        filetypes = (("PNG files", "*.png*"), ("JPG files", "*.jpg*")))

    return filePath

# Short 10 character conversion
def shortConversion():
    #update the buttons
    ASCII_SELECTION_SHORT_BUTTON.config(bg="Green")
    ASCII_SELECTION_LONG_BUTTON.config(bg="White")

    #get the image path and the file name
    filePath = getImagePath()

    if not filePath: return

    fileName = ntpath.basename(filePath).split(".")[0]

    #grab the image
    image = openImage(filePath)

    #convert to ascii
    convertToASCII(image, fileName, True)

    showOutputText(fileName)

# Long 70 character conversion
def longConversion():
    #update the buttons
    ASCII_SELECTION_LONG_BUTTON.config(bg="Green")
    ASCII_SELECTION_SHORT_BUTTON.config(bg="White")

    #get the image path and the file name
    filePath = getImagePath()
    fileName = ntpath.basename(filePath).split(".")[0]

    image = openImage(filePath)

    convertToASCII(image, fileName, False)
    showOutputText(fileName)

#Show a confirmation text
def showOutputText(fileName):
    SUCCESSFULL_OUTPUT_TEXT.config(text="Success! The file can be found at {0}{1}{2}".format(OUTPUT_PATH, fileName, EXTENSION))
    SUCCESSFULL_OUTPUT_TEXT.pack(pady=50)

# Buttons and Labels
TITLE = tk.Label(app, text=TITLE_TXT, font=(DEFAULT_FONT, 30))
TITLE.pack()

ASCII_SELECTION_SHORT_BUTTON = tk.Button(app, text=ASCII_SHORT_TXT, font=(DEFAULT_FONT, 20), command=shortConversion)
ASCII_SELECTION_SHORT_BUTTON.place(relx=0.3, rely=0.4)

ASCII_SELECTION_LONG_BUTTON = tk.Button(app, text=ASCII_LONG_TXT, font=(DEFAULT_FONT, 20), command=longConversion)
ASCII_SELECTION_LONG_BUTTON.place(relx=0.27, rely=0.5)

SUCCESSFULL_OUTPUT_TEXT = tk.Label(app, font=(DEFAULT_FONT, 20))

ABOUT_TEXT = tk.Label(app, text=ABOUT_TXT, font=(DEFAULT_FONT, 15))
ABOUT_TEXT.pack()
CREDIT_TEXT = tk.Label(app, text=CREDIT_TXT, font=(DEFAULT_FONT, 15))
CREDIT_TEXT.pack()

app.mainloop() # Start the app