"""
This script generates a text file starting from a given image by reading every pixel RGB values
and converting them in corresponding unicode characters.
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

def convert_to_txt(img_name, file_name):
    print(f"Converting '{img_name}' to text...")

    # Reading image
    image = Image.open(img_name)

    # Getting img dimensions
    n,m = image.size

    file_content = ""

    # Iterating each pixel and writing the corresponding characters
    x, y = 0,0
    for i in tqdm(range(n*m)):
        px = image.getpixel((x,y))
        for v in px:
            if v > 0:
                file_content += chr(v)
        # Advance to the next pixel
        x += 1
        if x >= n:
            x = 0
            y += 1
    
    with open(file_name, "w") as f:
        f.write(file_content)

def main():
    print("Enter the image path")
    img_name = input("> ")

    file_name = input("Enter a name for output file: ")

    convert_to_txt(img_name, file_name)

if __name__ == "__main__":
    main()