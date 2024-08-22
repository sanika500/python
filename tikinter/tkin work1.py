import tkinter as tk
from tkinter import messagebox
def celsius_farenheit():
    
    try:
       num1=float(entry1.get())
       result=num1*9/5+32
       messagebox.showinfo("result",result)
       
    except ValueError:
        messagebox.showerror("error","please enter valid numbers")
def farenheit_celsius():
    try:
        num1=float(entry1.get())
        result=num1-32*5/9
    except ValueError:
           messagebox.showerror("error","please enter valid numbers")

    
    
root=tk.Tk()
root.title("temperature convertor")
tk.Label(root,text="number1").grid(row=0,column=0,padx=10,pady=10)
entry1=tk.Entry(root)
entry1.grid(row=0,column=1,padx=10,pady=10)
entry2=tk.Entry(root)
entry2.grid(row=1,column=1,padx=10,pady=10)
add_button = tk.Button(root,text="convert celsius_farenheit",command=celsius_farenheit) 
cel=tk.Button(root,text="celsius",command=celsius_farenheit)
add_button.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
cel.grid(row=2,column=2,columnspan=2,padx=10,pady=10)
root.mainloop()