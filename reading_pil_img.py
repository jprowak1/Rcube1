# reading file pillow
from PIL import Image
import os
# image is 3020 square
CUBE_WIDTH = 1007
HALF_CUBE_WIDTH = CUBE_WIDTH/2
CUBE0_MID = HALF_CUBE_WIDTH
CUBE1_MID = CUBE0_MID + CUBE_WIDTH
CUBE2_MID = CUBE1_MID + CUBE_WIDTH
cube_smpling_pts = (CUBE0_MID, CUBE1_MID, CUBE2_MID)
# middle of each horizontal pixel
cub_img = os.path.join("/mnt/chromeos/MyFiles/Downloads/", "cubex.jpg")
with Image.open(cub_img) as im:
    im.load()
    print (im.size)
    for y in cube_smpling_pts:
        for x in cube_smpling_pts:
            print(f" location {x}, {y}")
            print (im.getpixel((x,y)))


