import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Toggle Button')
root.geometry('400x400')

is_on = True

def switch_on_off():
    global is_on

    if is_on:
        switch_label.config(text="Button is OFF",foreground="black")
        switch_button.config(image=off)
        is_on = False
    else:
        switch_label.config(text="Button is ON",foreground='green')
        switch_button.config(image=on)
        is_on = True

label_font = ('Helveltica',15,"bold")
switch_label = ttk.Label(root,text="Button is ON",foreground='green',font=label_font)
switch_label.pack(pady=20)

on = tk.PhotoImage(file='on.png')
off = tk.PhotoImage(file='off.png')

switch_button = tk.Button(root,image=on,bd=0,command=switch_on_off)
switch_button.pack(pady=40)

root.mainloop()
