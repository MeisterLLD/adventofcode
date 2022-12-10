detect = {20, 60, 100, 140, 180, 220}
curcycle = 1
X = 1
power = 0

for ligne in open('input10','r').readlines():

    if 'noop' in ligne:
        # début cycle
        if curcycle in detect:
            power += curcycle*X
        # fin cycle
        curcycle += 1


    elif 'addx' in ligne:
        nb = int(ligne.split(' ')[1])

        # début cycle
        if curcycle in detect:
            power += curcycle*X
        # fin cycle
        curcycle += 1

        # début cycle
        if curcycle in detect:
            power += curcycle*X
        X += nb
        # fin cycle
        curcycle += 1

print(power)



