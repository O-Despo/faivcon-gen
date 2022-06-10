#!/bin/python
from PIL import Image
import sys
import os

def main():
    print(sys.argv)
    inputFile = sys.argv[1]
    outputFolder = sys.argv[2]
    run(inputFile, outputFolder)

def run(pathInput, pathOutput):
    html_output = ""
    img_sizes = (32,57,76,96,128,192,228)
    base_img = Image.open(pathInput)
    pathOutput = os.path.abspath(pathOutput)
    print(pathOutput)

    for size in img_sizes:
        new_img = base_img.resize((size,size))
        path_end = f"favicon-{size}.png"

        new_path = pathOutput + "/" +  path_end
        new_img.resize((size,size))

        new_img.save(new_path)
        new_img.close()

        print(f"saved: {new_path}")

        html_output += f'<link rel="icon" href="/favicon/favicon-{size}.png" sizes="{size}x{size}">\n'

    with open(pathOutput + "/" + "icon.html", "w+") as file:
            file.writelines(html_output)

    print(html_output)
if __name__ == "__main__":
    main()
