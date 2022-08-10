"""
This script generates an image starting from a given text file by converting every character unicode value
into RGB values for the image pixels.
For details about conversion please read the README.md file.

Author: Ama
"""
from PIL import Image
import math
from tqdm import tqdm

def read_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    return content

def convert_to_img(content, img_name):
    print(f"Converting text file to image...")

    # Calculating img dimensions
    n = math.ceil(math.sqrt(len(content)/3))

    # Creating new blank image
    image = Image.new('RGB', (n,n))

    x,y = 0,0
    length = len(content)
    i = 0
    pos = 0
    value = [0,0,0]
    for c in tqdm(content):
        # If the value tuple is full, write the pixel and reset the tuple values
        if pos > 2:
            # Write the pixel to the image
            image.putpixel((x,y), tuple(value))
            # Reset values for the next write
            pos = 0
            value = [0,0,0]
            # Advance to the next pixel of the image
            x += 1
            if x >= n:
                x = 0
                y += 1
        # Write the character's ord into value[pos]
        value[pos] = ord(c)
        pos += 1 
        i += 1 # Character index
        if i == length:
            image.putpixel((x,y), tuple(value))
            
        
    image.save(f"./{img_name}")

def main():
    print("Enter the text file path")
    input_path = input("> ")

    content = read_file(input_path)

    print("Enter a name for output image")
    img_name = input("> ")

    convert_to_img(content, img_name)

if __name__ == "__main__":
    main()