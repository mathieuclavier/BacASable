#Programme de 1/2gt²
from math import*

def chutelibre(temps, attraction=9.81):
    resultat = round((1/2*attraction)*t*t,1)
    return resultat 

if __name__=="__main__":
    while True:
        t=float(input("Temps de chute: "))
        print("La distance de chute parcourue par le projectile est:",chutelibre(t), "m")