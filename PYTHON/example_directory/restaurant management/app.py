import tkinter as tk
from tkinter import messagebox

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        messagebox.showerror("Error","invalid expression")
        equation.set("")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__" :
    window = tk.Tk()
    window.title("Calculator")
    window.geometry("300x400")

    expression = ""
    equation = tk.StringVar()

    entry_field = tk.Entry(window,textvariable=equation,font=("Arial,18"),bd=10,borderwidth=4,insertwidth=2,width=14)
    entry_field.grid(row = 0 ,column = 0 , columnspan=4)

    buttons = [
        "7","8","9","/",
        "4","5","6","*",
        "1","2","3","-",
        "C","0","=","+"
    ]  

    row_val = 1
    col_val = 0

    for button in buttons:
        if button =="=":
            btn = tk.Button(window,text = button,padx =20,pady=20,font = ("Arial",14), bg = "green" ,fg = "white" ,command = equalpress)
        elif button =="C":
            btn = tk.Button(window,text = button,padx =20,pady=20,font = ("Arial",14),bg = "red" , fg = "white" ,command = clear)
        else :
            btn = tk.Button(window,text = button,padx =20,pady=20,font = ("Arial",14),command = lambda b=button:press(b))

        btn.grid(row = row_val,column = col_val,sticky = "nsew")
        col_val +=1
        if col_val >3:
           col_val = 0
           row_val +=1

    for i in range(5):
        window.grid_rowconfigure(i,weight=1)
    for j in range(4):
        window.grid_columnconfigure(j,weight=1)
    
    window.mainloop()

