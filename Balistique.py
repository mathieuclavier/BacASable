from math import*

print('Programme de balistque générale.')

step1 = input('Calculer la distance parcourue par le projectile ? [o/N]: ')
step1 = step1.strip().lower()
if step1.startswith('o'):

    v=float(input('Vélocitée initiale:'))
    a=float(input('Angle de tire: '))
    g=float(input('Atraction gravitationnelle: '))
    y=float(input('Hauteur initiale/au sol: '))

    d=round(((v/cos(a))/g)*(v*sin(a)+sqrt((v*sin(a))*(v*sin(a))+2*g*y)),1)
    print('La distance parcourue par le projectile est:',d,'m')

    reponse = input('Voulez-vous arrondir plus précisément? [o/N] ')
    reponse = reponse.strip().lower()

    if reponse.startswith('o'):
        x=int(input('A combien de chiffre voulez-vous arrondir?: '))
        d=round(((v/cos(a))/g)*(v*sin(a)+sqrt((v*sin(a))*(v*sin(a))+2*g*y)),x)
        print('La distance parcourue par le projectile est',d,'m')
    else:
        print('La distance parcourue par le projectile est',d,'m')

step2 = input('Calculer la hauteur maximale du projectile ? [o/N]')
step2 = step2.strip().lower()
if step2.startswith('o'):

    h=round((v*sin(a))*(v*sin(a))/(2*g)+y,1)

    print('La hauteur maximale atteinte par le prjectile est:',h,'m')

    reponse = input('Voulez-vous arrondir plus précisément? [o/N] ')
    reponse = reponse.strip().lower()

    if reponse.startswith('o'):
        x=int(input('A combien de chiffres voulez-vous arrondir?: '))
        h=round((v*sin(a))*(v*sin(a))/(2*g)+y,x)
        print('La hauteur maximale atteinte par le prjectile est:',h,'m')
    else:
        print('La hauteur maximale atteinte par le prjectile est:',h,'m')

step3 = input('Calculer la vitesse finale du projectile ?:')
step3 = step3.strip().lower()
if step3.startswith('o'):

    v=round(sqrt(2*g*y),1)
    print('La vitesse finale du projectile est:',v,'m/s')

    reponse = input('Voulez-vous arrondir plus précisément? [o/N] ')
    reponse = reponse.strip().lower()

    if reponse.startswith('o'):
        x=int(input('A combien de chiffre voulez-vous arrondir?: '))
        v=round(sqrt(2*g*y),x)
        print('La distance parcourue par le projectile est',v,'m')
    else:
        print('La distance parcourue par le projectile est',v,'m')

        "