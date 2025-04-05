import matplotlib.pyplot as plt
import numpy as np
import time
import tkinter as tk
from matplotlib.animation import FuncAnimation

fig, axs = plt.subplots()
# ar1 = np.array ([[0,.2,.4]])
tgl = True

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")
# Add a label widget
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack(pady=20)  # Add padding

def button_click():
    global tgl
    # label.config(text="Button Clicked = tgl")
    tgl = True
    im.set_array(np.random.rand(3,3))
    # im.set_array(ar1)

    print("HELLO")

button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

ar1 = np.array ([[0,.2,.4],
                [.1,.3,.5],
                [.6,.7,.8]])

im =axs.imshow(ar1, cmap = 'rainbow')


def animate(i):
    global tgl
    if tgl:
        tgl = False
        print("HI")
    return fig,


anim = FuncAnimation(fig, animate, frames=1, interval=200)

plt.show()
root.mainloop()