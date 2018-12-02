from math import*

v=float(input("Vélocitée initiale: "))
a=float(input("Angle de tire: "))
g=float(input("Atraction gravitationnelle: "))
y=float(input("Hauteur initiale/au sol: "))

d=round(((v/cos(a))/g)*(v*sin(a)+sqrt((v*sin(a))*(v*sin(a))+2*g*y)),1)
print("La distance parcourue par le projectile est:",d,"m")

reponse = input("Voulez-vous arrondir plus précisément? [o/N] ")
reponse = reponse.strip().lower()

if reponse.startswith('o'):
    x=int(input("A combien de chiffre voulez-vous arrondir?: "))
    d=round(((v/cos(a))/g)*(v*sin(a)+sqrt((v*sin(a))*(v*sin(a))+2*g*y)),x)
    print("La distance parcourue par le projectile est",d,"m")
else:
    print("La distance parcourue par le projectile est",d,"m")