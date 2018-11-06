from random import randint

def win_game(keep=None):
    doors   = ['Goat']*3
    voiture = randint(0,2)
    doors[voiture] = 'Car'

    # Candidate choose
    candidate   = randint(0,2)
    # Presentator cancelled one door (Useless here ...)
    presentator = 0
    for idx in range(len(doors)):
        if idx == candidate: continue
        if doors[idx] == 'Goat':
            presentator = idx
            break

    if keep == None: keep = (randint(0, 1) == 0)
    return 'Win' if ((doors[candidate] == 'Car') == keep) else 'Lose' 

count = 100000
exps = [win_game(True) for _ in range(count)]
print('Keep 1st door -> ' + str(float(exps.count('Win'))/float(count)))

exps = [win_game(False) for _ in range(count)]
print('Modify door -> ' + str(float(exps.count('Win'))/float(count)))

exps = [win_game() for _ in range(count)]
print('Coin -> ' + str(float(exps.count('Win'))/float(count)))
