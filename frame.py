from PIL import Image
import os

def comprasion(color):
    color = list(map(lambda x: x>127, color))
    return all(color)

def get_frame(img):
    width, height = img.size
    output = ""
    for y in range(height):
        for x in range(width):
            if comprasion(img.getpixel((x, y))):
                output += "X"
            else:
                output += " "
    return output

if __name__ == '__main__':
    width, height = os.get_terminal_size()
    newsize = width, height
    img = Image.open('img.jpeg')
    img = img.resize(newsize)
    print(get_frame(img))

