import tkinter as tk 
from tkinter import messagebox
def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result=num1+num2
        messagebox.showinfo("Result","The result of adding (num1)and (num2)is")   
    except ValueError:
        messagebox.showerror("Error","please enter valid numbers")
        
root=tk.Tk()
root.title("four function calculator")
tk.Label(root,text="Number1:").grid(row=0,column=0)
tk.Label(root,text="Number2:").grid(row=1,column=0) 
entry1=tk.Entry(root)         
entry1.grid(row=0,column=1)
entry2=tk.Entry(root)
entry2.grid(row=1,column=1)
add_button = tk.Button(root,text="Add",)

root.mainloop