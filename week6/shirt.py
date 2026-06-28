import sys
import os
import PIL
from PIL import Image
from PIL import ImageOps

if len(sys.argv) != 3 or not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")) or not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")) or os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
    sys.exit()

try:
    usi = Image.open(sys.argv[1])
    shirt = Image.open('shirt.png')
    size = shirt.size
    oui = PIL.ImageOps.fit(usi, size)
    oui.paste(shirt, None, shirt)
    oui.save(sys.argv[2])

except FileNotFoundError:
    sys.exit()