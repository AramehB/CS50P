import sys
from PIL import Image, ImageOps

if len(sys.argv) == 3:
    x = (sys.argv[1]).lower()
    y = (sys.argv[2]).lower()
    if (x.endswith(".jpg") and y.endswith(".jpg")) or (x.endswith(".jpeg") and y.endswith(".jpeg")) or (x.endswith(".png") and y.endswith(".png")):
        try:
            shirt = Image.open("shirt.png")
            size = shirt.size
            photo = Image.open(x)
            photo = ImageOps.fit(photo, size=[size[0], size[1]])
            photo.paste(shirt,shirt)
            photo.save(y, format=None)
        except FileNotFoundError:
            sys.exit("Error: The file was not found.")
    else:
        sys.exit("Input and output have different extensions, or are not valid image formats.")
elif len(sys.argv) <= 3:
    sys.exit("Error: Too few command-line arguments.")
else:
    sys.exit("Error: Too many command-line arguments.")
