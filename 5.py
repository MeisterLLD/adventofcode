

with open('input5','r') as f:
    # Préparation des piles
    pile = [ []  for i in range(9) ]

    for i in range(8):
        lec = f.readline()
        for i in range(9):
            if lec[4*i+1] != ' ': pile[i].append(lec[4*i+1])

    for x in pile:
        x.reverse()

    # Opérations
    f.readline()
    f.readline()
    for ligne in f.readlines():
        nb = int(ligne.split('move')[1].split('from')[0])
        deb = int(ligne.split('move')[1].split('from')[1].split('to')[0])-1
        fin = int(ligne.split('move')[1].split('from')[1].split('to')[1])-1

        for i in range(nb):
            obj = pile[deb].pop()
            pile[fin].append(obj)

    print([x[-1] for x in pile])