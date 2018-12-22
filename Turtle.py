from turtle import *
while 1>0:
    x=int(input("Longueur du côté: "))
    c=int(input("Nombre de côtés: "))
    for i in range(c):
        forward(x)
        a=360/c
        left(a)