from tkinter import *
from PIL import Image,ImageTk

win=Tk()
win.geometry('900x900')
win.title('canvas')

c=Canvas(win,bg='pink',height=100,width=200)
# image_=PhotoImage(file='agu.gif')
# img=c.create_image(500,300,anchor='center',image=image_)
c.pack()
x1,x2,y1,y2=20,50,20,50
line=c.create_line(x1,y1,x2,y2)
oval=c.create_oval(x1+20,y1+10,x2+20,y2+10,fill='blue')
arc=c.create_arc(x1+40,y1+30,x2+40,y2+30)
rect=c.create_rectangle(100,30,120,50)

def moveit():
    c.move(rect,10,10)

b=Button(win,text='move',height='3',width=40,command=moveit)
b.pack()

win.mainloop()

# Canvas操作：
# var.create_image()
# var.create_line()
# var.create_oval()
# var.create_arc()
# var.move(var,x,y)