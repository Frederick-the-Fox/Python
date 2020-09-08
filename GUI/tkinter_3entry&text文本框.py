from tkinter import *

win=Tk()
win.title('my tkinter')
win.geometry('200x200')

e=Entry(win,show='*')
e.pack()

def insert_point():
    t.insert('insert',e.get())

def insert_end():
    t.insert('end',e.get())


b1=Button(win,text='insert point',width=15,height=2,command=insert_point)
b1.pack()

b2=Button(win,text='insert end',command=insert_end)
b2.pack()

t=Text(win,height=2)
t.pack()

win.mainloop()



# Entry的定义：
# 第一个是窗口，然后可以定义输入以后显示的形式，比如说*

