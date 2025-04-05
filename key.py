import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot(np.random.rand(10))

def onclick(event):
    print(f'helloooo button={event.key}, x={event.xdata}, y={event.ydata}')

fig.canvas.mpl_connect('key_press_event', onclick)

plt.show()