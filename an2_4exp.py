import matplotlib.pyplot as plt
import numpy as np
import time
import tkinter as tk
import random
from matplotlib.animation import FuncAnimation
iml =[]
tgl = True
# subplot arrangement- half will be unused
fig, axs = plt.subplots(4,3)
# also need np.array 6,3,3, call it cube_arr=

cube_arr0=np.full((3,3),.1,float)
cube_arr1=np.full((3,3),.2,float)
cube_arr2=np.array([[.3,.3,.3],[.3,.3,.3],[.3,.3,.3]])
cube_arr3=np.full((3,3),0.4,float)
cube_arr4=np.full((3,3),0.5,float)
cube_arr5=np.full((3,3),0.6,float)
cube_arr=[cube_arr0,cube_arr1, cube_arr2, cube_arr3, cube_arr4, cube_arr5]


axs[0,0].set_axis_off()
axs[0,2].set_axis_off()
axs[1,0].set_axis_off()
axs[1,2].set_axis_off()
axs[3,0].set_axis_off()
axs[3,2].set_axis_off()



# TODO need 6 ims
im0 = axs[0,1].imshow(cube_arr[2],cmap= 'rainbow')
im1 = axs[1,1].imshow(cube_arr[2],cmap= 'rainbow')
im2 = axs[2,0].imshow(cube_arr[2],cmap= 'rainbow')
# im2 = axs[2,0].imshow(np.random.rand(3,3),cmap= 'rainbow')

im3 = axs[2,1].imshow(cube_arr[2],cmap= 'rainbow')
im4 = axs[2,2].imshow(cube_arr[2],cmap= 'rainbow')
im5 = axs[3,1].imshow(cube_arr[2],cmap= 'rainbow')

iml = [im0,im1,im2,im3,im4,im5]

def button_click():
    global tgl
    # label.config(text="Button Clicked = tgl")
    tgl = True
    
#TODO add radio button, add_to_q button, rm_fr_q butt
#TODO add functions to add_to_q, rm_fr_q
#Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")
# Add a label widget
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack(pady=20)  # Add padding
button = tk.Button(root, text="Click Me", command=button_click)
button.pack()


# TODO add function to update cube_arr

def animate(i):
    global tgl,iml,cube_arr
    # if tgl :
    print(f"tlg TRUE")
    num = random.randint(0,5)
    ind = random.randint(0,5)
        # iml[num].set_array(cube_arr[num])
        #im2.set_data(np.random.rand(3,3))
    iml[ind].set_data(cube_arr[num])
    print(f"cube_arr[{num}] = {cube_arr[num]}")   
        # tgl = False
    return fig,

anim = FuncAnimation(fig, animate, frames=1, interval=500)
print(f"cube_arr[0] = {cube_arr[0]}")
plt.show()
# root.mainloop()