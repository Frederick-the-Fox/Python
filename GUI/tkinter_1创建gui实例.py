from tkinter import*#导入tkinter模块

tk=Tk()#创建gui应用程序的主窗口

label=Label(tk,text ='Welcome') 
button=Button(tk,text='Click me')
#添加控件或者GUI应用程序
label.pack()
button.pack()
#控件布局
tk.mainloop()#进入主事件循环，等待响应用户触发事件