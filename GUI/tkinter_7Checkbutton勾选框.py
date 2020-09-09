from tkinter import *

win=Tk()
win.geometry('900x900')
win.title('Checkbox')

l=Label(win,width=30,height=2,bg='pink',text='Decide please!')
l.pack()

v1=IntVar()
v2=IntVar()

def print_selection():
    if v1.get() & v2.get():
        l.config( text='I love both Py and Cpp')
    elif v1.get():
        l.config(text='I love Python only')
    elif v2.get():
        l.config(text='I love Cpp only')
    else:
        l.config(text='I do not like these languages')
        

c1=Checkbutton(win,text='Python',variable=v1,onvalue=1,offvalue=0,command=print_selection)
c2=Checkbutton(win,text='Python',variable=v2,onvalue=1,offvalue=0,command=print_selection)
c1.pack()
c2.pack()

win.mainloop()