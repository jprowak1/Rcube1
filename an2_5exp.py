import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import random
import time
from matplotlib.animation import FuncAnimation

tgl = True
fig, axs = plt.subplots(1,2)
cube_arr=[]
iml = []
# also need np.array 6,3,3, call it cube_arr=
cube_arr0=np.array([[1,5,5],[5,8,5],[5,5,8]])
cube_arr1=np.full((3,3),5)
# cube_arr= [cube_arr0, cube_arr1]
cube_arr.append(cube_arr0)
cube_arr.append(cube_arr1)
im0 = axs[0].imshow(cube_arr0,cmap= 'rainbow')
im1 = axs[1].imshow(cube_arr1,cmap= 'rainbow')
iml.append(im0)
iml.append(im1)
# iml = [im0,im1]
# iml[0].set_data(np.random.rand(3,3))

def button_click():
    global tgl
    # label.config(text="Button Clicked = tgl")
    tgl = True
    # im0.set_data(np.random.rand(3,3))
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
    global tgl,iml, cube_arr0
    if tgl :
        num = random.randint(0,1)
        # iml[num].set_data(np.array(cube_arr0))
        mylist =[[1,5,9],[1,5,9],[9,5,1]]
        # iml[num].set_data(np.array(mylist))
        iml[num].set_data(np.random.randint(9,size=(3,3)))

        #im2.set_data(np.random.rand(3,3))
        #im2.set_array(cube_arr[num])

        print(f"num ={num}")
        tgl = False
    return fig,

anim = FuncAnimation(fig, animate, frames=1, interval=100)
print(f"cube_arr[0] = {cube_arr[0]}")
plt.show()
root.mainloop()