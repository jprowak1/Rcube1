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
        tot = 0
        # calculate difference
        for pxl, ref in zip(smpl,n[2]):
            tmp =pxl-ref
            if tmp <0 :
                diff = -tmp
                # keep it positive
            else:
                diff = tmp
            tot +=diff
        print(f" diff for {n[1]} is {tot}")




cub_img = os.path.join("/mnt/chromeos/MyFiles/Downloads/", "cubex.jpg")
with Image.open(cub_img) as im:
    im.load()
    print (im.size)
    for y_ind, y in enumerate(cube_smpling_pts):
        for x_ind,x  in enumerate(cube_smpling_pts):
            print(f"============\n location {x_ind}, {y_ind}\n============")
            cube_smpl = im.getpixel((x,y))
            print (cube_smpl)
            get_color(cube_smpl)


