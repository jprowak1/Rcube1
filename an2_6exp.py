import matplotlib.pyplot as plt
import numpy as np
import random
import time
from matplotlib.animation import FuncAnimation

fig, axs = plt.subplots(3)
iml = []
count = 0
cube_arr =[]
cube_arr0=np.array(([1,5,5],[5,8,5],[5,5,8]))
cube_arr1=np.array(([[8,5,2],[5,8,2],[8,5,8]]))
cube_arr2=np.full((3,3),6)
cube_arr=[cube_arr0,cube_arr1,cube_arr2]

im0 = axs[0].imshow(cube_arr0,cmap= 'rainbow')
im1 = axs[1].imshow(cube_arr1,cmap= 'rainbow')
im2 = axs[2].imshow(cube_arr0,cmap= 'rainbow')
iml=[im0,im1,im2]

def animate(i):
    global count, cube_arr,iml
    num = random.randint(0,2)
    ind = random.randint(0,2)
    iml[num].set_data(cube_arr[ind])
    print(f"num ={num}, cube_arr = {cube_arr[num]}")
    return fig,

anim = FuncAnimation(fig, animate, interval=500)
plt.show()