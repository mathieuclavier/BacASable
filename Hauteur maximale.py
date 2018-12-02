from math import*

v=float(input("Vélocitée initiale: "))
a=float(input("Angle de tire: "))
g=float(input("Atraction gravitationnelle: "))
y=float(input("Hauteur initiale/au sol: "))

h=round((v*sin(a))*(v*sin(a))/(2*g)+y,1)

print("La hauteur maximale atteinte par le prjectile est:",h,"m")

reponse = input("Voulez-vous arrondir plus précisément? [o/N] ")
reponse = reponse.strip().lower()

if reponse.startswith('o'):
    x=int(input("A combien de chiffres voulez-vous arrondir?: "))
    h=round((v*sin(a))*(v*sin(a))/(2*g)+y,x)
    print("La hauteur maximale atteinte par le prjectile est:",h,"m")
else:
    print("La hauteur maximale atteinte par le prjectile est:",h,"m")
