# reading file pillow
from PIL import Image
import os
cub_img = os.path.join("/mnt/chromeos/MyFiles/Downloads/", "cubex.jpg")
with Image.open(cub_img) as im:
    print (im.size)
    print (im.getpixel((200,200)))
    print (im.getpixel((210,200)))
    print (im.getpixel((220,200)))


