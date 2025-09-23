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
lifo =[]
rdy = True
lst_but =0
# red 6.2, yell 4.8, green 3, blue 2, orange 5.6, white 9.9
#     0
#     1
#  2  3  4
#     5  
red,green,yellow,orange,blue,white =[6.2,3,4.8,5.6,2,9.9]
cube_arr = np.empty((6,3,3))
#------------------------------------
# Patterns to evaluate move commands
#------------------------------------
# cube_l_tst =np.full((6,3,3),white)
# cube_l_tst[3,0,0], cube_l_tst[3,1,0], cube_l_tst[3,2,0] = red, yellow, blue
# cube_l_tst =np.full((6,3,3),white)
# cube_l_tst[3,0,0], cube_l_tst[3,1,0], cube_l_tst[3,2,0] = red, yellow, blue




#------------------------------------



def reset_cube_array():
    global cube_arr
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

def r_tst():
    global cube_arr
    cube_r_tst =np.full((6,3,3),white)
    cube_r_tst[3,0,2], cube_r_tst[3,1,2], cube_r_tst[3,2,2] = red, yellow, blue     
    cube_arr = cube_r_tst
    
def l_tst():
    global cube_arr
    cube_l_tst =np.full((6,3,3),white)
    cube_l_tst[3,0,0], cube_l_tst[3,1,0], cube_l_tst[3,2,0] = red, yellow, blue
    cube_arr = cube_l_tst
    
def u_tst():
    global cube_arr
    cube_u_tst =np.full((6,3,3),white)
    cube_u_tst[3,0] = [red, yellow, blue]   
    cube_arr = cube_u_tst
    
def d_tst():
    global cube_arr
    cube_d_tst =np.full((6,3,3),white)
    cube_d_tst[3,2] = [red, yellow, blue]       
    cube_arr = cube_d_tst

def f_tst():
    global cube_arr
    cube_f_tst =np.full((6,3,3),white)
    cube_f_tst[4,:,0] = [red, yellow, blue]       
    cube_arr = cube_f_tst
    
def b_tst():
    global cube_arr
    cube_b_tst =np.full((6,3,3),white)
    cube_b_tst[1,0,:] = [red, yellow, blue]       
    cube_arr = cube_b_tst

def pr_var():
    rb_var = variable.get()
    print(f"Var = {rb_var}")
    lb.insert(tk.END,rb_var)
    # enable lst_move button

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

def lst_move():
    global cube_arr, lifo
    if lifo:
        cube_arr = np.copy(lifo.pop())
    else:
        print("LIFO is empty")
    # print(" Popping {lifo}")


def upd_cube(mv):
    global cube_arr,lifo
    lifo.append(np.copy(cube_arr))
    
    if(mv == "U"):
        tmp3, tmp4, tmp0,tmp2 =np.copy(cube_arr[3,0]), np.copy(cube_arr[4,0]), np.copy(cube_arr[0,2]),np.copy(cube_arr[2,0])
        cube_arr[2,0],cube_arr[3,0] , cube_arr[4,0], cube_arr[0,2] = tmp3, tmp4, np.flip(tmp0), np.flip(tmp2)
        cube_arr[1]= np.rot90(cube_arr[1])
        cube_arr[1]= np.rot90(cube_arr[1])
        cube_arr[1]= np.rot90(cube_arr[1])
    elif (mv == "R"):
        tmp5, tmp3, tmp1,tmp0 = np.copy(cube_arr[5,:,2]), np.copy(cube_arr[3,:,2]),np.copy(cube_arr[1,:,-1]),np.copy(cube_arr[0,:,2])
        cube_arr[3,:,2], cube_arr[1,:,2], cube_arr[0,:,2],cube_arr[5,:,2] = tmp5, tmp3, tmp1,tmp0
        cube_arr[4] =np.rot90(cube_arr[4])
    elif (mv == "D"):
        tmp3, tmp4, tmp0,tmp2 =np.copy(cube_arr[3,2]), np.copy(cube_arr[4,2]), np.copy(cube_arr[0,0]),np.copy(cube_arr[2,2])
        cube_arr[2,2],cube_arr[3,2],cube_arr[4,2],cube_arr[0,0] = np.flip(tmp0),tmp2,tmp3,np.flip(tmp4)
        cube_arr[5] = np.rot90(cube_arr[5])
        cube_arr[5] = np.rot90(cube_arr[5])
        cube_arr[5] = np.rot90(cube_arr[5])  
    elif (mv == "L"):
        tmp5, tmp3, tmp1,tmp0 = np.copy(cube_arr[5,:,0]), np.copy(cube_arr[3,:,0]),np.copy(cube_arr[1,:,0]),np.copy(cube_arr[0,:,0])
        cube_arr[3,:,0], cube_arr[1,:,0], cube_arr[0,:,0],cube_arr[5,:,0] = tmp1, (tmp0), (tmp5),tmp3
        cube_arr[2] = np.rot90(cube_arr[2])

    elif (mv == "B"):
        tmp1, tmp2, tmp4,tmp5 = np.copy(cube_arr[1,0,:]), np.copy(cube_arr[2,:,0]), np.copy(cube_arr[4,0,:]),np.copy(cube_arr[5,2,:])
        cube_arr[1,0,:],cube_arr[2,:,0], cube_arr[4,2,:], cube_arr[5,2,:] = np.flip(tmp4),np.flip(tmp1),tmp5, np.flip(tmp2)
        cube_arr[0] = np.rot90(cube_arr[0])

    elif (mv == "F"):
        tmp2, tmp1, tmp4, tmp5 = np.copy(cube_arr[2,:,2]), np.copy(cube_arr[1,2,:]), np.copy(cube_arr[4,:,0]), np.copy(cube_arr[5,0,:])
        cube_arr[2,:,2], cube_arr[1,2,:], cube_arr[4,:,0], cube_arr[5,0,:] = tmp5, np.flip(tmp2), (tmp1),  np.flip(tmp4)
        cube_arr[3] =np.rot90(cube_arr[3])

    return

root = tk.Tk()
root.title("Radiobutton")
root.geometry("360x480")
add_to_queue = tk.Button(root, text="add RadBut to queue", command=pr_var)
add_to_queue.pack()
rm_fr_queue = tk.Button(root, text="rm RadBut from queue", command=rm_var)
rm_fr_queue.pack()
res_cube = tk.Button(root, text="reset cube", command=res_cube)
res_cube.pack()
lst_move=tk.Button(root, text="undo move", command=lst_move)
lst_move.pack()
# test buttons for commands
r_tst =tk.Button(root, text="R test cube", command=r_tst)
r_tst.pack()
l_tst =tk.Button(root, text="L test cube", command=l_tst)
l_tst.pack()
u_tst =tk.Button(root, text="U test cube", command=u_tst)
u_tst.pack()
d_tst =tk.Button(root, text="D test cube", command=d_tst)
d_tst.pack()
f_tst =tk.Button(root, text="F test cube", command=f_tst)
f_tst.pack()
b_tst =tk.Button(root, text="B test cube", command=b_tst)
b_tst.pack()
# b_tst =tk.Button(root, text="B test cube", command=b_tst)
# b_tst.pack()
lb = tk.Listbox(root)
lb.pack()
choices = ["R", "L", "U","D", "F", "B"]
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