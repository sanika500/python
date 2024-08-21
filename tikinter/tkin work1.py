import tkinter as tk
from tkinter import messagebox
def celsius_farenheit():
    
    try:
       num1=float(c*9/5+32)
    except ValueError:
        return" invalid input"
def farenheit_celsius():
    try:
        num2=float(f-32)*5/9
    except ValueError:
        return"invalid input"
# def convert():
#     if c in f:
#      return(celsius_farenheit)
#     else:
#         return(farenheit_celsius)
    
    
root=tk.Tk()
root.title("temperature convertor application")
tk.Label(root,text="temp in cel or far").grid(row=0,column=1)
# tk.Label(root,text="farenheit_celsius").grid(row=1,column=0)
entry1=tk.Entry(root)
entry1.grid(row=0,column=1)
# entry2=tk.Entry(root)
# entry2.grid(row=1,column=1)
add_button = tk.Button(root,text="convert celsius_farenheit",command="celsius_farenheit") 
add_button.grid(row=2,column=0,columnspan=2)
add_button1 = tk.Button(root,text="convert farenheit_celsius",command="farenheit_celsius") 
add_button1.grid(row=3,column=0,columnspan=2)
root.mainloop()