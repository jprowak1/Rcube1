import tkinter as tk

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
root.mainloop()