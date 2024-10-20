import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
var = tk.IntVar()
flag = tk.BooleanVar()

def clicked():
    print("Clicked")
    text = var.get()
    print(var)

tk.Button(textvariable=var, text="Click me", width=10, command=clicked).pack()
e = tk.Entry(textvariable=var, width=10)
e.pack()
tk.Checkbutton(variable=flag, text="flag").pack()


root.mainloop()