import tkinter as tk
root=tk.Tk()
root.title("details")
label1=tk.Label(root,text="Name")
label2=tk.Label(root,text="Class")
label3=tk.Label(root,text="Age")
Text1=tk.Entry()
Text2=tk.Entry()
Text3=tk.Entry()
label1.pack()
Text1.pack()
label2.pack()
Text2.pack()
label3.pack()
Text3.pack()
button=tk.Button(root,text="submit")
button.pack()
root.mainloop()