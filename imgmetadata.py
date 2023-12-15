# Az aktuális könyvtárban található JPG és PNG fájlokat kilistázza a metaadataikkal együtt

import os
from PIL import Image
from PIL.ExifTags import TAGS

directory = os.getcwd()

for filename in os.listdir(directory):
    print()
    print(filename)
    filestat = os.stat(directory + '/' + filename)
    print(' - Size: ' + str(filestat.st_size) + ' bytes')
    if filename.endswith('.jpg') or filename.endswith('.JPG') or filename.endswith('.jpeg') or filename.endswith('.JPG'):
        for (k,v) in Image.open(directory + '/' + filename)._getexif().items():    
            print(' - %s: %s' % (TAGS.get(k), v))
    elif filename.endswith('.png') or filename.endswith('.PNG'):
        im = Image.open(directory + '/' + filename)
        im.load()
        print(im.info)
        