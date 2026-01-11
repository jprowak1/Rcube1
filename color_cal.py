# reading file pillow
from PIL import Image
import os
# image is 3020 square
CUBE_WIDTH = 100
# middle of each horizontal pixel
HALF_CUBE_WIDTH = CUBE_WIDTH/2
CUBE0_MID = HALF_CUBE_WIDTH
CUBE1_MID = CUBE0_MID + CUBE_WIDTH
CUBE2_MID = CUBE1_MID + CUBE_WIDTH
#cube_smpling_pts = (CUBE0_MID, CUBE1_MID, CUBE2_MID)
cube_smpling_pts = (CUBE0_MID,)
img_tup = ("cube0.jpeg", "cube1.jpeg", "cube2.jpeg", "cube3.jpeg", "cube4.jpeg", "cube5.jpeg")
#img_tup = ("cube1.jpeg",)


def get_color (smpl):
    RED = (181,46,40)
    GR = (0,220,0)
    #BL = (112,185,220)
    BL = (0,0,255)
    OR = (230,104,27)
    YE = (150,180,0)
    #WH = (115,110,99
    WH = (255,255,255)
    red_int, gr_int,bl_int, or_int,ye_int, wh_int = (0,0,0,0,0,0)
    COL_TUP =  (  (red_int, "RED", RED),  (gr_int, "GREEN", GR), (bl_int, "BL", BL),
                    (or_int, "ORANGE", OR), (ye_int, "YELLOW", YE), (wh_int, "WHITE", WH) )
    for n in COL_TUP:
        print(f"comparing to {n[1]}")
        tot = 0
        indx, tmp,diff = 0,0,0
        # calculate difference in the rgb color vector
        for indx, (pxl, ref) in enumerate(zip(smpl,n[2])):
            print(f"indx {indx}, pxl {pxl}, ref {ref}")
            tmp =pxl-ref
            if tmp <0 :
                #print(f"{tmp} is neg")
                #keep it positive
                tmp = -tmp
                #print(f"new element diff  is {diff}")
            tot +=tmp
        print(f" FINAL diff for {n[1]} is {tot}")

for cub_fil in img_tup:
    print(f"#############\nchecking cubeface {cub_fil}\n#############\n")
    #cub_img = os.path.join("/mnt/chromeos/MyFiles/Downloads/cubepics_A0", cub_fil)
    cub_img = os.path.join("/mnt/chromeos/MyFiles/Downloads/cubepics_cal", cub_fil)
    with Image.open(cub_img) as im:
        im.load()
        print (im.size)
        for y_ind, y in enumerate(cube_smpling_pts):
            for x_ind,x  in enumerate(cube_smpling_pts):
                print(f"============\n location {x_ind},{x}, -- {y_ind},{y}\n============")
                cube_smpl = im.getpixel((x,y))
                print (cube_smpl)
                get_color(cube_smpl)


