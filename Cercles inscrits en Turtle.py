from turtle import*
x=int(input("Nombre de côtés: "))
l=int(input("Longueur de côté: "))
n=int(input("Nombre de cercles: "))
for i in range(n):
  for i in range(x):
    forward(l)
    left(360/x)
  x=x-10
  
