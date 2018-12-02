from math import*

g=float(input("Atraction gravitationnelle: "))
y=float(input("Hauteur initiale/au sol: "))

v=round(sqrt(2*g*y),1)

reponse = input("Voulez-vous arrondir plus précisément? [o/N] ")
reponse = reponse.strip().lower()

if reponse.startswith('o'):
    x=int(input("A combien de chiffre voulez-vous arrondir?: "))
    d=round(sqrt(2*g*y),x)
    print("La distance parcourue par le projectile est",d,"m")
else:
    print("La distance parcourue par le projectile est",d,"m")