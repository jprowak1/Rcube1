import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.animation import FuncAnimation
fig, axs = plt.subplots()
ar1 = np.array ([[0,.2,.4],
            [.1,.3,.5],
            [.6,.7,.8]])


im =axs.imshow(ar1, cmap = 'rainbow')


def animate(i):
    im.set_array(np.random.rand(3,3))
    return fig,


anim = FuncAnimation(fig, animate, frames=1, interval=100)

plt.show()