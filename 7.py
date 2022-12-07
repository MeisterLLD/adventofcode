with open('input7','r') as f:

    sizedir = {"root": 0}
    peres = {"root":None}

    curdir = "root"
    f.readline()

    while True:
        ligne = f.readline()
        if ligne == '': break

        elif '$ ls' in ligne:
            continue

        elif '$ cd' in ligne:
            gotodir = ligne.split('cd')[1][1:-1]
            if gotodir != '..':
                curdir = curdir + '/' + gotodir
            else:
                curdir = curdir[::-1].split('/',1)[1][::-1]

        elif 'dir ' in ligne:
            newlocaldir = ligne.split('dir')[1][1:-1]
            newdir = curdir + '/' + newlocaldir
            peres[newdir] = curdir
            if newdir not in sizedir: sizedir[newdir] = 0

        else:
            taillefich = int(ligne.split(' ')[0])
            suiteperes = curdir
            sizedir[suiteperes] += taillefich
            while suiteperes != 'root':
                suiteperes = peres[suiteperes]
                sizedir[suiteperes] += taillefich

#7a
tot = 0
for x in sizedir.items():
    taille = x[1]
    if taille <= 100000:
        tot += taille
print(tot)


#7b
capa = 70000000
needdel = 30000000 -(capa - sizedir['root'])

from math import inf
rep = inf
for x in sizedir:
    if sizedir[x]>needdel and sizedir[x]<rep: rep = sizedir[x]
print(rep)
