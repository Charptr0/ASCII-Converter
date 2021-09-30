from PIL import Image

# 3.75
ASCII_STR_LONG = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.'''

# 25
ASCII_CHAR_SHORT = '''@#$%?*+;:,.'''

def openImage(path): return Image.open(path)
def convertToGrayScale(image): return image.convert("L")
def resizeImage(image, width, height): return image.resize((width, height))


