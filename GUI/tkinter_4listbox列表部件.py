from tkinter import*

win=Tk()
win.geometry('200x200')
win.title('listbox')

# 定义Button并且定义函数内容
def print_selection():
    value=lb.get(lb.curselection())
    var1.set(value)
b=Button(win,text='print selection',width=15,height=2,command=print_selection)
b.pack()
# 定义label与变量1
var1=StringVar()
l=Label(win,bg='yellow',width=4,textvariable=var1)
l.pack()
#定义lb与变量2
var2=StringVar()
var2.set((11,22,33,44,55,66))
# 列表里面的初始变量需要是元组类型。
lb=Listbox(win,listvariable=var2)
list_items=[1,2,3,4]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
# insert里面的元素第一个是插入的目标位置，第二个是插入的内容。
lb.delete(2)
lb.pack()

# win.mainloop()
# Listbox的操作:
# var.curselection()
# var.get()
# ps:常用组合用法：var.get(var.curselection)
# var.insert()
# var.delete()
