import matplotlib.pyplot as plt
import numpy as np
import random
import time
from matplotlib.animation import FuncAnimation
import tkinter as tk


fig, axs = plt.subplots(4,3)

iml = []
count = 0
const_arr =[]
rdy = True
# red 6.2, yell 4.8, green 3, blue 2, orange 5.6, white 9.9
#     0
#     1
#  2  3  4
#     5  
red,green,yellow,orange,blue,white =[6.2,3,4.8,5.6,2,9.9]
cube_arr = np.empty((6,3,3))

def reset_cube_array():
    global cube_arr
    # for i ,val in enumerate([9.9,2,3,4.8,5.5, 6.2]):
    for i, val in enumerate([white,orange,green,yellow,blue,red]):
        cube_arr[i] = np.full((3,3),val  )
    print(f" RESETING cube_arr  {cube_arr}")

const_arr0=np.array(([1,5,5],[5,8,5],[5,5,8]))


off_lst = [(0,0),(0,2),(1,0),(1,2),(3,0),(3,2)]
on_list =[(0,1),(1,1),(2,0),(2,1),(2,2), (3,1)]
for j in off_lst:
    axs[j].set_axis_off()

# initialize the cube faces - due to a bug, we have to uses the res_cube button to set them 
# to their initial state
count=0
for j in on_list:
    im =axs[j].imshow(const_arr0, cmap= 'gist_ncar')
    # im=axs[j].imshow(cube_arr[count], cmap= 'rainbow')
    iml.append(im)

def init():
    pass
#     for i in range(0,6):
#         iml[i].set_data(cube_arr[i])


def pr_var():
    rb_var = variable.get()
    print(f"Var = {rb_var}")
    lb.insert(tk.END,rb_var)

def rm_var():
    rmv = lb.get(0)
    print(f"rmv = {rmv}")
    upd_cube(rmv)
    lb.delete(0)    

def res_cube():
    global rdy,cube_arr
    reset_cube_array()
    for i in range(6):
        iml[i].set_data(cube_arr[i])
    rdy = True

def upd_cube(mv):
    global cube_arr
    if(mv == "L"):
        tmp3, tmp4, tmp0,tmp2 =np.copy(cube_arr[3,0]), np.copy(cube_arr[4,0]), np.copy(cube_arr[0,2]),np.copy(cube_arr[2,0])
        #cube_arr[2,0],cube_arr[3,0] , cube_arr[4,0], cube_arr[0,2] = cube_arr[3,0], cube_arr[4,0],cube_arr[0,2], cube_arr[2,0]
        #cube_arr[2,0],cube_arr[3,0] , cube_arr[4,0], cube_arr[0,2,:] = cube_arr[3,0], cube_arr[4,0],cube_arr[0,2], tmp2
        cube_arr[2,0],cube_arr[3,0] , cube_arr[4,0], cube_arr[0,2] = tmp3, tmp4, tmp0, tmp2


        
       

    print(f"cube2 = {cube_arr[2]}\n cube0 = {cube_arr[0]}")
    return

root = tk.Tk()
root.title("Radiobutton")
root.geometry("360x480")
add_to_queue = tk.Button(root, text="add RB to queue", command=pr_var)
add_to_queue.pack()
rm_fr_queue = tk.Button(root, text="rm RB from queue", command=rm_var)
rm_fr_queue.pack()
res_cube = tk.Button(root, text="reset cube", command=res_cube)
res_cube.pack()
lb = tk.Listbox(root)
lb.pack()
choices = ["R", "L", "U","D"]
variable = tk.StringVar(root, f"{choices[0]}")
for choice in choices:
    tk.Radiobutton(
        root,
        text=choice,
        variable=variable,
        value=choice,
    ).pack()

reset_cube_array()

def animate(i):
    global rdy,cube_arr
    if rdy:
        global const_arr,iml
        # num = random.randint(0,5)
        # ind = random.randint(0,5)
        # iml[num].set_data(const_arr[ind])
        for i in range(6):
            iml[i].set_data(cube_arr[i])

        # print(f"ind ={ind}, const_arr = {const_arr[num]}")
        return fig,
        rdy = False

anim = FuncAnimation(fig, animate, init_func= init, interval=800)
plt.show()
root.mainloop()