# reading file pillow
from PIL import Image
import os
# image is 3020 square
CUBE_WIDTH = 1007
# middle of each horizontal pixel
HALF_CUBE_WIDTH = CUBE_WIDTH/2
CUBE0_MID = HALF_CUBE_WIDTH
CUBE1_MID = CUBE0_MID + CUBE_WIDTH
CUBE2_MID = CUBE1_MID + CUBE_WIDTH
cube_smpling_pts = (CUBE0_MID, CUBE1_MID, CUBE2_MID)

def get_color (smpl):
    RED = (255,0,0)
    GR = (0, 255,0)
    BL = (0,0,255)
    OR = (200,80,80)
    YE = (0, 255,255)
    WH = (255,255,255)
    red_int, gr_int,bl_int, or_int,ye_int, wh_int = (0,0,0,0,0,0)
    COL_TUP =  (  (red_int, "RED", RED),  (gr_int, "GREEN", GR), (bl_int, "BL", BL),
                    (or_int, "ORANGE", OR), (ye_int, "YELLOW", YE), (wh_int, "WHITE", WH) )
    for n in COL_TUP:
        print(f"comparing to {n[1]}")




cub_img = os.path.join("/mnt/chromeos/MyFiles/Downloads/", "cubex.jpg")
with Image.open(cub_img) as im:
    im.load()
    print (im.size)
    for y in cube_smpling_pts:
        for x in cube_smpling_pts:
            print(f" location {x}, {y}")
            cube_smpl = im.getpixel((x,y))
            print (cube_smpl)
            get_color(cube_smpl)


