# ImageCutter
A Python program providing a way to slice up a image.

## Examples
Cut a .jpg image to 4x4 (width x height) square slices
```
python3 Splitter.py 4 4 image.jpg
```
Cut a .png image to 10x1 stripes and store them to a directory `dir`
```
python3 Splitter.py 10 1 image.png --to dir
```
