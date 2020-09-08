from tkinter import*

win=Tk()
win.title('radiobutton')
win.geometry('900x400')

var=StringVar()
l1=Label(win,text='Which is the correct pronunciaton')
l1.pack()
l=Label(win,bg='yellow',width=40,text='please choose one of these following selections')
l.pack()

def print_selectionA():
    l.config(text='Congratulations!',bg='green')
def print_selectionB():
    l.config(text='What are you F**king thingking about?',bg='red')
def print_selectionC():
    l.config(text='Serious?????',bg='purple')
r1=Radiobutton(win,text='[paɪθɑn]',command=print_selectionA)
r2=Radiobutton(win,text='[paɪθen]',command=print_selectionB)
r3=Radiobutton(win,text='[I love xjx]',command=print_selectionC)

r1.pack()
r2.pack()
r3.pack()

win.mainloop()