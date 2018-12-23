from math import*
from turtle import*

x=-600
y=-300
z=0
zoom=19

def tracage(x,y,z,zoom):
    up()
    goto(x,y)
    for i in range(800):
        for e in range(800):
            z=z+1
    d=(z*z)/1000000000000*zoom
    x=x+0.5
    y=y+d
    goto(x,y)

input()