from math import *
from Fraction import *

while True:
  a = Fraction(input("a= "))
  b = Fraction(input("b= "))
  c = Fraction(input("c= "))
  
  if a==0:
    print("Le polynôme n'est pas ")
    print("un trinôme du second degré ")
    
  else:
    delta= b**2-4*a*c
    print("discriminent= " delta)
    
    if delta>0:
      print("Le polynôme à 2 racines: ")
      print("x1 =" Fraction(b**2-sqrt(delta))/2*a))
      print("x2 =" Fraction(b**2+sqrt(delta))/2*a))
      
      
    
