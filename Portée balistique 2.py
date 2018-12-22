from math import *

def portee(velocite, angle, attraction=9.81, hauteur=0, precision=1):
    rangle = radians(angle)
    resultat = round(
        (velocite*cos(rangle)/attraction)*(velocite*sin(rangle)+sqrt((velocite*sin(rangle))**2+2*attraction*hauteur))
        , precision
    )
    return resultat

if __name__=="__main__":
    while True:
        v=float(input("Vélocitée initiale: "))
        a=float(input("Angle de tire: "))
        g=float(input("Atraction gravitationnelle: "))
        y=float(input("hauteur initiale: "))
        print("resultat: ", portee(v, a, g, y))

        continuer = input("Voulez vous continuer? [o/N]").strip().lower()
        if not continuer.startswith('o'):
            break

    print("Fini")