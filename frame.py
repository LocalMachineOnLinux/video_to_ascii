from PIL import Image
import os
import numpy as np

def comprasion(color):
    color = list(map(lambda x: x>127, color))
    return np.all(color)

def get_frame(pixels, size):
    width, height = size
    output = ""
    for x in range(width):
        for y in range(height):
            if comprasion(pixels[x][y]):
                output += "X"
            else:
                output += " "
    return output

if __name__ == '__main__':
    width, height = os.get_terminal_size()
    newsize = width, height
    img = Image.open('img.jpeg')
    img = img.resize(newsize)
    pixels = np.array(img.getdata()).reshape(*img.size, 3)
    print(get_frame(pixels, newsize))

