import sys
import os
from PIL import Image

try:
    sourcepath = sys.argv[1]
    destinationpath =sys.argv[2]

    if not os.path.exists(destinationpath): os.mkdir(destinationpath)

    for files in os.listdir(sourcepath):
        #if '.jpg' in files:
        if files.endswith(".jpg"):
            img = Image.open(os.path.join(sourcepath,files))
            img_name = os.path.splitext(os.path.join(destinationpath,files))[0]+'.png'
            img.save(img_name)

except Exception as err:
    print(err.message)

