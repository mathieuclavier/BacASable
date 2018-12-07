from turtle import*

while 1>0:
  x=int(input("Nombre de côtés: "))
  l=int(input("Longueur de côté: "))
  n=int(input("Nombre de cercles: "))
  e=1
  reponse = input('Dimentions des cercles exponentielle? [o/N] ')
  reponse = reponse.strip().lower()
  for i in range(n):
    if reponse.startswith('o'):
     e=e+1
    for i in range(x):
      forward(l)
      left(360/x)
    x=x-10*e
  input("Recommencer [Entrée]:")
  clear()
