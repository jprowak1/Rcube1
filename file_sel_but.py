import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Radiobutton")
root.geometry("360x480")
def load_cube_face():
    filename = filedialog.askopenfilename(
        initialdir="/", # Start directory (use "/" for root or "C:/" on Windows)
        title="Select a file",
        filetypes=(
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ) # Filter file types
    )
load_cf_but = tk.Button(root, text="Select cube face_file", command=load_cube_face)
load_cf_but.pack()
root.mainloop()