import tkinter as tk
from tkinter import filedialog
from ASCIIConverter import *
from texts import *
import ntpath

RESOLUTION = "800x800"
DEFAULT_FONT = "Calibri"

app = tk.Tk()
app.geometry(RESOLUTION)
app.resizable(False, False)
app.title(TITLE_TXT)


# Open the window for the user to choose an image
def getImagePath():
    filePath = filedialog.askopenfilename(initialdir = "./", 
        title = "Select a to convert to ASCII art", 
        filetypes = (("PNG files", "*.png*"), ("JPG files", "*.jpg*")))

    return filePath

# Resize the image depending on the inputs
def parseNewDimensions(image, new_width, new_height):
    ERR_DIM_TEXT.place_forget()

    # If width and height box are filled
    if new_width and new_height:
        try: #make sure the inputs are integers
            new_width = int(new_width) 
            new_height = int(new_height)
        except: #display err and return original img
            ERR_DIM_TEXT.place(relx=0.12, rely=0.7)
            return image

        return resizeImage(image, new_width, new_height)

    #If width is filled
    elif new_width:
        try:
            new_width = int(new_width)
        except: 
            ERR_DIM_TEXT.place(relx=0.12, rely=0.7)
            return image

        return resizeImage(image, new_width, image.height)

    #If height is filled
    elif new_height:
        try:
            new_height = int(new_height)
        except:
            ERR_DIM_TEXT.place(relx=0.12, rely=0.7)
            return image

        return resizeImage(image, image.width, new_height)
    
    #if none are filled, return the original img
    else: return image

# Short 10 character conversion
def shortConversion():
    #update the buttons
    ASCII_SELECTION_SHORT_BUTTON.config(bg="Green")
    ASCII_SELECTION_LONG_BUTTON.config(bg="White")

    #get the image path and the file name
    filePath = getImagePath()

    if not filePath: return

    #grab the image
    image = openImage(filePath)

    fileName = ntpath.basename(filePath).split(".")[0]

    new_width = CHANGE_WIDTH_INPUT_BOX.get()
    new_height = CHANGE_HEIGHT_INPUT_BOX.get()

    resized_image = parseNewDimensions(image, new_width, new_height)

    #convert to ascii
    convertToASCII(resized_image, fileName, True)

    #display the filename
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

    new_width = CHANGE_WIDTH_INPUT_BOX.get()
    new_height = CHANGE_HEIGHT_INPUT_BOX.get()

    resized_image = parseNewDimensions(image, new_width, new_height)

    convertToASCII(resized_image, fileName, False)

    showOutputText(fileName)

#Show a confirmation text
def showOutputText(fileName):
    SUCCESSFULL_OUTPUT_TEXT.config(text="Success! The file can be found at {0}{1}{2}".format(OUTPUT_PATH, fileName, EXTENSION))
    SUCCESSFULL_OUTPUT_TEXT.pack(pady=50)

# Buttons and Labels
TITLE = tk.Label(app, text=TITLE_TXT, font=(DEFAULT_FONT, 30))
TITLE.pack()

ASCII_SELECTION_SHORT_BUTTON = tk.Button(app, text=ASCII_SHORT_TXT, font=(DEFAULT_FONT, 20), command=shortConversion)
ASCII_SELECTION_SHORT_BUTTON.place(relx=0.3, rely=0.3)

ASCII_SELECTION_LONG_BUTTON = tk.Button(app, text=ASCII_LONG_TXT, font=(DEFAULT_FONT, 20), command=longConversion)
ASCII_SELECTION_LONG_BUTTON.place(relx=0.27, rely=0.4)

CHANGE_WIDTH_TEXT = tk.Label(app, text="New Width", font=(DEFAULT_FONT, 15))
CHANGE_WIDTH_TEXT.place(relx=0.3, rely=0.5)

CHANGE_HEIGHT_TEXT = tk.Label(app, text="New Height", font=(DEFAULT_FONT, 15))
CHANGE_HEIGHT_TEXT.place(relx=0.3, rely=0.55)

CHANGE_WIDTH_INPUT_BOX = tk.Entry(app, width=20)
CHANGE_WIDTH_INPUT_BOX.place(relx=0.45, rely=0.51)

CHANGE_HEIGHT_INPUT_BOX = tk.Entry(app, width=20)
CHANGE_HEIGHT_INPUT_BOX.place(relx=0.45, rely=0.56)

SUCCESSFULL_OUTPUT_TEXT = tk.Label(app, font=(DEFAULT_FONT, 20))
ERR_DIM_TEXT = tk.Label(app, text=ERR_TXT, font=(DEFAULT_FONT, 20), fg="red")

ABOUT_TEXT = tk.Label(app, text=ABOUT_TXT, font=(DEFAULT_FONT, 15))
ABOUT_TEXT.pack()
CREDIT_TEXT = tk.Label(app, text=CREDIT_TXT, font=(DEFAULT_FONT, 15))
CREDIT_TEXT.pack()

app.mainloop() # Start the app