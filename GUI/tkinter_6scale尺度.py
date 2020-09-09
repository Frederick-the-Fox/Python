from tkinter import *

win=Tk()
win.title('scale')
win.geometry( '900x900')

l=Label(win,width=30,height=2,bg='yellow',text='Please have a try')
l.pack()

def demo(v):
    l.config(text='you have selected'+v,bg='green')
#这个函数里面必须有这个传入值，不然没有办法成功调用。

s=Scale(win,label='push me',# 滑动条的名称
from_=5,to=11, # 取值范围，其中from为敏感函数，所以重新定义为from_
orient=HORIZONTAL,# 方向
length=200,# 单位不是字符，而是像素
showvalue=0,# 是否将选中的数值显示在条的上方，1/0
tickinterval=3,# 标签的单位长度，也就是每次隔多少显示一个标度
resolution=0.01,# 精确到小数点后几位。
command=demo
)
s.pack()

win.mainloop()