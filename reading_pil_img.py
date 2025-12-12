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
img_tup = ("cube0.jpeg", "cube1.jpeg", "cube2.jpeg", "cube3.jpeg", "cube4.jpeg", "cube5.jpeg")


def get_color (smpl):
    RED = (181,46,40)
    GR = (100,171,51)
    BL = (112,185,220)
    OR = (230,104,27)
    YE = (208,209,30)
    WH = (115,110,90)
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
                #print(f"{tmp} is neg")
                diff = -tmp
                # keep it positive
                #print(f"new diff  is {diff}")
            else:
                diff = tmp
            tot +=diff
        print(f" diff for {n[1]} is {tot}")

for cub_fil in img_tup:
    cub_img = os.path.join("/mnt/chromeos/MyFiles/Downloads/cubepics_A0", cub_fil)
    with Image.open(cub_img) as im:
        im.load()
        print (im.size)
        for y_ind, y in enumerate(cube_smpling_pts):
            for x_ind,x  in enumerate(cube_smpling_pts):
                print(f"============\n location {x_ind}, {y_ind}\n============")
                cube_smpl = im.getpixel((x,y))
                print (cube_smpl)
                get_color(cube_smpl)


