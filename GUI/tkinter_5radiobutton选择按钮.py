from tkinter import *

win=Tk()
win.title('radiobutton')
win.geometry('900x400')

l=Label(win,width=20,height=2,bg='yellow',text='Please choose one of these selections')
l.pack()

var=StringVar()
def print_selection():
    l.config(text='you have selected'+var.get())
r1=Radiobutton(win,text='A:[paiθan]',variable=var,value='A',command=print_selection)
r2=Radiobutton(win,text='A:[paiθen]',variable=var,value='B',command=print_selection)
r3=Radiobutton(win,text='A:[paiθin]',variable=var,value='C',command=print_selection)
r1.pack()
r2.pack()
r3.pack()
win.mainloop()