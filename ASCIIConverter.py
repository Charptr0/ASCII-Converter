from PIL import Image
import os

# 3.75
ASCII_CHAR_LONG = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''

# 25
ASCII_CHAR_SHORT = " .:-=+*#%@"

OUTPUT_PATH = "outputs/"
EXTENSION = ".txt"

def openImage(path): return Image.open(path)
def _convertToGrayScale(image): return image.convert("L")
def resizeImage(image, width, height): return image.resize((width, height))

def convertToASCII(image : Image, fileName, ASCII_SHORT):
    grayScaleImage = _convertToGrayScale(image)

    cols, rows = grayScaleImage.size #get the dimensions of the image
    pixels = grayScaleImage.load()

    if not os.path.exists(OUTPUT_PATH): os.mkdir(OUTPUT_PATH)

    with open(OUTPUT_PATH + fileName + EXTENSION, "w") as f:
        for r in range(rows):
            for c in range(cols):
                pixel_color = pixels[c, r]

                if ASCII_SHORT: f.write(ASCII_CHAR_SHORT[pixel_color // 25])
                else: f.write(ASCII_CHAR_LONG[pixel_color // 3.75])

            f.write("\n")

print(len(ASCII_CHAR_LONG))