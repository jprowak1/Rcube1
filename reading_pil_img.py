# reading file pillow
from PIL import Image
import os
# image is 3020 square
CUBE_WIDTH = 1000
# middle of each horizontal pixel
HALF_CUBE_WIDTH = CUBE_WIDTH/2
CUBE0_MID = HALF_CUBE_WIDTH
CUBE1_MID = CUBE0_MID + CUBE_WIDTH
CUBE2_MID = CUBE1_MID + CUBE_WIDTH
cube_smpling_pts = (CUBE0_MID, CUBE1_MID, CUBE2_MID)
img_tup = ("cube0.jpeg", "cube1.jpeg", "cube2.jpeg", "cube3.jpeg", "cube4.jpeg", "cube5.jpeg")
#img_tup = ("cube3.jpeg",)


def get_color (smpl):
    # identify the pxl (smpl) color by comparing to the reference colors
    RED = (220,6,4)
    GR = (20,220,70)
    #BL = (112,185,220)
    BL = (0,90,220)
    OR = (231,124,31)
    YE = (206,176,6)
    #WH = (115,110,99
    WH = (230,230,200)
    red_int, gr_int,bl_int, or_int,ye_int, wh_int = (0,0,0,0,0,0)
    COL_TUP =  (  (red_int, "RED", RED),  (gr_int, "GREEN", GR), (bl_int, "BL", BL),
                    (or_int, "ORANGE", OR), (ye_int, "YELLOW", YE), (wh_int, "WHITE", WH) )
    min = 1000
    for n in COL_TUP:
        #print(f"comparing to {n[1]}")
        tot = 0
        # calculate difference. must use zip or numpy, since subtraction is not supported for tuples
        for pxl, ref in zip(smpl,n[2]):
            #print(f" pxl {pxl}, ref {ref}")
            tmp =pxl-ref
            if tmp <0 :
                #print(f"{tmp} is neg")
                diff = -tmp
                # keep it positive
                #print(f"new diff  is {diff}")
            else:
                diff = tmp
            #print(f" diff = {diff}")
            tot +=diff
        if tot < min:
            #print (f"tot {tot} is less than min {min}")
            min = tot
            color_result = n
    #print(f" color_result = {n[1]}")
    return color_result

for cub_fil in img_tup:
    print(f"#############\nchecking cubeface {cub_fil}\n#############")
    #cub_img = os.path.join("/mnt/chromeos/MyFiles/Downloads/cubepics_A0", cub_fil)
    cub_img = os.path.join("/mnt/chromeos/MyFiles/Downloads/cubepics_A2", cub_fil)
    with Image.open(cub_img) as im:
        im.load()
        print (im.size)
        # loop over all rows and columns for all 9 cube faces, grabbing a pxl in the approx center of cube face
        for y_ind, y in enumerate(cube_smpling_pts):
            for x_ind,x  in enumerate(cube_smpling_pts):
                #print(f"============\n location {x_ind},{x}, -- {y_ind},{y}\n============")
                cube_smpl = im.getpixel((x,y))
                #print (cube_smpl)
                cube_face_color = get_color(cube_smpl)
                print (f" ============= CUBE_FACE_COLOR = {cube_face_color[1]}")


