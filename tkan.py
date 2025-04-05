import matplotlib.pyplot as plt
import numpy as np
import time
import tkinter as tk
from matplotlib.animation import FuncAnimation
global tgl

fig, axs = plt.subplots()
ar1 = np.array ([[0,.2,.4]])
tgl = True
# # Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")
# # Add a button widget
def button_click():
    global tgl
    label.config(text="Button Clicked = tgl")
    tgl = not tgl
    print ("tgl = ", tgl)

# Add a label widget
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack(pady=20)  # Add padding
button = tk.Button(root, text="Click Me", command=button_click)
button.pack()



im =axs.imshow(ar1, cmap = 'rainbow')


def animate(i):
    global tgl
    if tgl:
        im.set_array(np.random.rand(3,3))
        tgl = False
        return fig,


anim = FuncAnimation(fig, animate, frames=1, interval=300)

plt.show()
root.mainloop()