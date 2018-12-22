from turtle import*
from math import*
x=-800
y=-300
t=0
zoom=float(input("Zoom [10;25]: "))
up()
goto(x,y)
down()
for i in range(8000):
    for e in range(800):
        t=t+1
    d=(4/3*pi*t**3)/10**zoom
    x=x+0.5
    y=y+d
    goto(x,y)
input()