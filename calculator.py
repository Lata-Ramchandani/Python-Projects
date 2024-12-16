from tkinter import *

root = Tk()
root.resizable(0,0) # prevents window from resizing
root.title("Calculator")
root.geometry("300x350")

user_input = StringVar() # user_input is StringVar() that stores the text displayed in the Entry widget
display = Entry(root,textvariable=user_input,font=("Arial",19),bd=6,justify="right")
display.grid(row=0,column=0,columnspan=5)

def btn_clicked(value):
    current = user_input.get()
    if value == 'C':
        user_input.set("")
    elif value == 'CE':
        user_input.set(current[:-1])
    elif value == '=':
        try:
            if value == '=':
                result = eval(current)
                user_input.set(result)
        except Exception:
            user_input.set("Error")
    elif value == '+/-':
        if current:
            if current.startswith('-'):
                user_input.set(current[1:]) #removes - sign
            else:
                user_input.set("-" + current) # adds - sign
    else:
        user_input.set(current + value)

btns = [
    ['CE','C','+/-','%'],
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['.','0','=','+']
]

for i,row in enumerate(btns):
    for j,text in enumerate(row):
        Button(root,text=text,font=('Arial',14),width=5,height=2,
               command=lambda value=text:btn_clicked(value)
               ).grid(row=i+1,column=j)

root.mainloop()