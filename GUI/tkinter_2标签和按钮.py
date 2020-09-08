from tkinter import*
#导入tkinter模块
win=Tk()#建立窗口
win.title('mywindow')#为窗口起名字
win.geometry('200x100')#定义长与宽，注意是字符串，中间是小写字母x

strvar=StringVar()#由于要实现变化的功能，所以要变量，定义一个字符串变量
l=Label(win,textvariable=strvar,bg='blue',font=('Arial',12),width=15,height=2)#定义label 参数的格式就参考这个例子，尤其要注意的是font
l.pack()#把定义好的label放到win里面

i=False#定义一个判断变量
def hit_me():#定义函数可供按钮按下的时候调用
    global i#声明全局变量
    if i==False:
        strvar.set('One Piece')#在tkinter中的字符串操作都有自己的函数
        i=True
    else:
        strvar.set('')
        i=False
b=Button(win,text='hit me',width=13,height=2,command=hit_me)# 参数规范，注意最后的command
b.pack()#一定要记得放置

win.mainloop()

StringVar的操作：
.set('content')

# Button的定义元素内容：
# 第一个首先要是窗口的内容，然后可以定义宽度、高度、文字、文字变量、调用的函数等等
