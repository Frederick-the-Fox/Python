from graphics import *
def main():
    win=GraphWin('click me!')
    for i in range (10):
        p=win.getMouse()
        print('You clicked at :',p.getX(),p.getY())


if __name__=='__main__':
    main()