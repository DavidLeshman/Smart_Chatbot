import tkinter as tk  
from tkinter import ttk  
win = tk.Tk()  
win.title("Smart Chatbot")# Label  
Lbl = ttk.Label(win, text = "Button Not Click ")  
Lbl.pack()# Click event  
def click(): action.configure(text = "Ask your Q now")  
Lbl.configure(foreground = 'red')  
Lbl.configure(text = 'Ask me anything')# Adding Button  


action = ttk.Button(win, text = "Click me to ask anything", command = click)  
action.pack()

win.mainloop()











