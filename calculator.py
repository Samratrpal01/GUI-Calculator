import tkinter
from tkinter import *

win = Tk() 
win.geometry("600x700+100+200")  
win.resizable(0, 0)
win.configure(bg="#17161b")
win.title("Calculator")
equation=""


def show(value):
    global equation
    if(value=="√"):
        equation+="**0.5"
        
    elif(value=="%%"):
        equation+="*0.01"   
    else:
        equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="Error Found in Expression"
            equation=""
    label_result.config(text=result)

label_result=Label(win,width=25,height=2,text="",font=("arial",30))
label_result.pack()


Button(win,text="√",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#7B68EE",command=lambda:show("√")).place(x=10,y=100)
Button(win,text="Mod",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("%")).place(x=150,y=100)
Button(win,text="Pow",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("**")).place(x=290,y=100)
Button(win,text="Percent",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("%%")).place(x=430,y=100)

Button(win,text="C",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=200)
Button(win,text="/",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("/")).place(x=150,y=200)
Button(win,text="*",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("*")).place(x=290,y=200)
Button(win,text="%",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("%")).place(x=430,y=200)

Button(win,text="7",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#7B68EE",command=lambda:show("7")).place(x=10,y=300)
Button(win,text="8",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("8")).place(x=150,y=300)
Button(win,text="9",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("9")).place(x=290,y=300)
Button(win,text="-",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("-")).place(x=430,y=300)

Button(win,text="4",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#7B68EE",command=lambda:show("4")).place(x=10,y=400)
Button(win,text="5",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("5")).place(x=150,y=400)
Button(win,text="6",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("6")).place(x=290,y=400)
Button(win,text="+",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("+")).place(x=430,y=400)

Button(win,text="1",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#7B68EE",command=lambda:show("1")).place(x=10,y=500)
Button(win,text="2",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("2")).place(x=150,y=500)
Button(win,text="3",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("3")).place(x=290,y=500)
Button(win,text="0",width=13,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("0")).place(x=10,y=600)


Button(win,text=".",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#7B68EE",command=lambda:show(".")).place(x=290,y=600)
Button(win,text="=",width=5,height=5,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda: calculate()).place(x=430,y=500)


win.mainloop()

