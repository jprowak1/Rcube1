import matplotlib.pyplot as plt
import numpy as np
import random
import time
from matplotlib.animation import FuncAnimation

fig, axs = plt.subplots(6)
iml = []
count = 0
cube_arr =[]
cube_arr0=np.array(([1,5,5],[5,8,5],[5,5,8]))
cube_arr1=np.array([[8,5,2],[5,8,2],[8,5,8]])
cube_arr2=np.array([[6,6,6],[6,6,6],[6,6,6]],float)
cube_arr3=np.full((3,3),2)
cube_arr4=np.full((3,3),4)
cube_arr5=np.full((3,3),8)
cube_arr=[cube_arr0,cube_arr1,cube_arr2,cube_arr3, cube_arr4,cube_arr5]

im0 = axs[0].imshow(cube_arr0,cmap= 'rainbow')
im1 = axs[1].imshow(cube_arr1,cmap= 'rainbow')
im2 = axs[2].imshow(cube_arr1,cmap= 'rainbow')
im3 = axs[3].imshow(cube_arr1,cmap= 'rainbow')
im4 = axs[4].imshow(cube_arr1,cmap= 'rainbow')
im5 = axs[5].imshow(cube_arr1,cmap= 'rainbow')
iml=[im0,im1,im2,im3,im4,im5]

def animate(i):
    global count, cube_arr,iml
    num = random.randint(0,5)
    ind = random.randint(0,5)
    iml[num].set_data(cube_arr[ind])
    print(f"ind ={ind}, cube_arr = {cube_arr[num]}")
    return fig,

anim = FuncAnimation(fig, animate, interval=100)
plt.show()