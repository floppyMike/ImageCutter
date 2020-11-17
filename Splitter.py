#!/usr/bin/env python
# coding: utf-8


from PIL import Image
import argparse
import sys
import os


parser = argparse.ArgumentParser(description = "Cuts a image file into blocks of a given width and height.")

parser.add_argument("width", type = int, help = "Blocks width.")
parser.add_argument("height", type = int, help = "Blocks height.")
parser.add_argument("file", type = str, nargs = '+', help = "File you want to cut.")
parser.add_argument("--to", type = str, help = "Destination to output to.")

args = parser.parse_args()


path = "" if args.to is None else args.to 
files = args.file
width = args.width
height = args.height


for file in files:
    im = Image.open(file)

    img_w, img_h = im.size
    slice_w, slice_h = img_w / width, img_h / height

    for h in range(0, height):
        for w in range(0, width):
            box_x, box_y = w * slice_w, h * slice_h
            box = (box_x, box_y, box_x + slice_w, box_y + slice_h)
            o = im.crop(box)
            p = os.path.join(path, "IMG_Split_%dx%d" % (w, h) + '_' + os.path.basename(file)) + ".png"
            print("Saving " + p)
            o.save(p, format='PNG')
