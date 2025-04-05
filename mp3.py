import matplotlib.pyplot as plt
import numpy as np
import time
fig, axs = plt.subplots(3,3)
ar1 = np.array ([[0,.2,.4],
            [.1,.3,.5],
            [.6,.7,.8]])
ar2 = np.array ([[.2,.4,.99],
             [.4,.4,.4],
             [.4,.4,.4]])

axs[0,1].imshow(ar1, cmap = 'rainbow')
axs[1,0].imshow(ar1, cmap = 'rainbow')
axs[1,1].imshow(ar1, cmap = 'rainbow')
axs[1,2].imshow(ar1, cmap = 'rainbow')
im =axs[2,1].imshow(ar1, cmap = 'rainbow')
for i in range(0,3):
    for j in range(0,3):
        axs[i,j].set_axis_off()

# plt.ion()
# # time.sleep(3)
# im.set_data(ar2)
# fig.canvas.draw()
# time.sleep(20)
# time.sleep(2)
im.set_data(ar1)
plt.draw()
plt.show()


