import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Radiobutton")
root.geometry("200x200")
def load_cube_face():
    moves = {"F", "B", "U", "D", "L", "R"}
    nums = {"1", "2", "3"}
    fname = filedialog.askopenfilename(
        initialdir="/My files", # Start directory (use "/" for root or "C:/" on Windows)
        title="Select a file",
        filetypes=(
            ("Text files", "*.txt"),
            ("All files", "*.*")
        )
    )
    # read the entire txt file
    with open(fname, 'r') as myfile:
        content = myfile.read()
        # loop over the entire txt file, char at a time
        for chr in content:
            # check for UDRLFB chars
            if (chr in moves) :
                prev_chr = chr
                print(chr)
            elif (chr in nums):
                # repear chars for number 2 or 3
                cntr =int(chr) -1
                for _ in  range (cntr):
                    print (prev_chr)
            # and push onto queue

load_cf_but = tk.Button(root, text="Select cube face_file", command=load_cube_face)
load_cf_but.pack()
root.mainloop()