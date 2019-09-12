from math import *
from fractions import Fraction

while True:
  a = Fraction(input("a= "))
  b = Fraction(input("b= "))
  c = Fraction(input("c= "))
  
  if a==0:
    print("Le polynome n'est pas ")
    print("un trinome du 2nd deg. ")
    
  else:
    delta= b**2-4*a*c
    print("discriminent= ", delta)
    
    if delta>0:
      print("Le polynome a 2 racines: ")
      x1= Fraction(b**2-(sqrt(delta))/2*a)
      x2= Fraction(b**2+(sqrt(delta))/2*a)
      print("x1 =", x1)
      print("x2 =", x2)

    elif delta==0:
      x0= Fraction(-b/2*a)
      print("Le polynome a une racine: x0= ", x0)

    else:
      print("Le polynome n a pas de racine réelle.")
