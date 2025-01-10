import tkinter as tk
root = tk.Tk()

def click():
    click_count.set(click_count.get()+1)
click_count = tk.IntVar()


button = tk.Button(root, text ="CLICKME", command = click)
button.pack()

label = tk.Label(root,textvariable=click_count)

label.pack()

root.mainloop()
