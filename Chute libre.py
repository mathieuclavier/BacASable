#Programme de 1/2gt²
from math import*

g=float(input("Acceleration gravitationnelle: "))
t=0
t=float(input("Temps de chute: "))

d=round((1/2*g)*t*t,1)
print("La distance de chute parcourue par le projectile est:",d,"m")

n=int(input("Arrondir la veleur à combien de chiffres ?:"))
d=round((1/2*g)*t*t,n)
print("La distance de chute parcourue par le projectile est:",d,"m")