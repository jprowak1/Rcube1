import matplotlib.pyplot as plt
import numpy as np
import random
import time
from matplotlib.animation import FuncAnimation
import tkinter as tk


fig, axs = plt.subplots(6)
iml = []
count = 0
const_arr =[]
const_arr0=np.array(([1,5,5],[5,8,5],[5,5,8]))
const_arr1=np.array([[8,5,2],[5,8,2],[8,5,8]])
const_arr2=np.array([[6,6,6],[6,6,6],[6,6,6]],float)
const_arr3=np.full((3,3),2)
const_arr4=np.full((3,3),4)
const_arr5=np.full((3,3),8)
const_arr=[const_arr0,const_arr1,const_arr2,const_arr3, const_arr4,const_arr5]
root = tk.Tk()
root.title("Radiobutton")
root.geometry("360x480")

choices = ["R", "L", "U","D"]
variable = tk.StringVar(root, f"{choices[0]}")
for choice in choices:
    tk.Radiobutton(
        root,
        text=choice,
        variable=variable,
        value=choice,
    ).pack(anchor="w", padx=10, pady=5)

def pr_var():
    rb_var = variable.get()
    print(f"Var = {rb_var}")
    lb.insert(tk.END,rb_var)

def rm_var():
    rmv = lb.get(0)
    print(f"rmv = {rmv}")
    lb.delete(0)    

add_to_queue = tk.Button(root, text="add RB to queue", command=pr_var)
add_to_queue.pack()
rm_fr_queue = tk.Button(root, text="rm RB from queue", command=rm_var)
rm_fr_queue.pack()
lb = tk.Listbox()
lb.pack()

im0 = axs[0].imshow(const_arr0,cmap= 'rainbow')
im1 = axs[1].imshow(const_arr1,cmap= 'rainbow')
im2 = axs[2].imshow(const_arr1,cmap= 'rainbow')
im3 = axs[3].imshow(const_arr1,cmap= 'rainbow')
im4 = axs[4].imshow(const_arr1,cmap= 'rainbow')
im5 = axs[5].imshow(const_arr1,cmap= 'rainbow')
iml=[im0,im1,im2,im3,im4,im5]

def animate(i):
    global const_arr,iml
    num = random.randint(0,5)
    ind = random.randint(0,5)
    iml[num].set_data(const_arr[ind])
    print(f"ind ={ind}, const_arr = {const_arr[num]}")
    return fig,

anim = FuncAnimation(fig, animate, interval=100)
plt.show()
root.mainloop()