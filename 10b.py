curcycle = 1
X = 1
crt = ''

def actualise(crt,X,curcycle):
    if curcycle % 40 == 1: crt += '\n'

    if (curcycle-1)%40 in {X-1,X,X+1} : crt += '#'
    else: crt += '.'

    return crt


for ligne in open('input10','r').readlines():
    if 'noop' in ligne:
        # début cycle
        crt = actualise(crt,X,curcycle)
        print(X,curcycle)

        # fin cycle
        curcycle += 1

    elif 'addx' in ligne:
        nb = int(ligne.split(' ')[1])

        # début cycle
        crt = actualise(crt,X,curcycle)
        print(X,curcycle)

        # fin cycle
        curcycle += 1

        # début cycle
        crt = actualise(crt,X,curcycle)
        print(X,curcycle)
        X += nb
        # fin cycle
        curcycle += 1


print(crt)



