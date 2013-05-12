from random import randint
from Tkinter import *
def D(n):
    x=y=x2=y2=0; s=n;
    if(n&1==0): y2=-1;
    while(s>0):
        stv=s&3;
        if(stv==1): x2,y2=x-y2,x2+y;
        if(stv==2): x2,y2=-y2-1,x2;
        if(stv==3): x2,y2=x2-y-1,y2+x;
        x,y=x+y+1,y-x;
        s>>=1;
        print x,y
    return x2,y2+1;
xoffset=450
yoffset=350
width=600
height=600
root=Tk()
m=Canvas(root,width=width,height=height,bg='black')
m.pack()
for i in xrange(1000000):
    n=D(i)
    m.create_line(n[0]+xoffset,n[1]+yoffset,n[0]+xoffset+1,n[1]+yoffset+1,fill='#'+str(i).ljust(6,'0'))
    m.update()
root.mainloop()
