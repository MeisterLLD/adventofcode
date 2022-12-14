from math import inf
xmin,ymin = inf,0
xmax,ymax = 0,0

xsource,ysource = 500,0

with open('input14','r') as fic:
    for ligne in fic.read().splitlines():
        path = ligne.split(' -> ')
        for s in path:
            x,y = tuple(map(int, s.split(',') ))
            if x > xmax: xmax = x
            if x < xmin: xmin = x
            if y > ymax: ymax = y
n = ymax+1
m = xmax+1

## Fabrication de la carte
carte = [ [0 for j in range(m+1)] for i in range(n+1) ]
carte[ysource][xsource] = '+'

with open('input14','r') as fic:
    for ligne in fic.read().splitlines():
        path = ligne.split(' -> ')
        for i in range(len(path)-1):
            xdeb,ydeb = tuple(map(int, path[i].split(',') ))
            xfin,yfin = tuple(map(int, path[i+1].split(',') ))

            if xfin != xdeb:
                if xfin < xdeb: xfin, xdeb = xdeb, xfin
                for j in range(xdeb,xfin+1):
                    carte[ydeb][j] = 1
            elif yfin != ydeb:
                if yfin < ydeb: yfin, ydeb = ydeb, yfin
                for k in range(ydeb,yfin+1):
                    carte[k][xdeb] = 1
##

# def affiche(carte):
#     for i in range(0,ymax):
#         ligne = ''
#         for j in range(xmin,xmax):
#             if carte[i][j] == '+': ligne += '+'
#             elif carte[i][j] == 0: ligne += '.'
#             elif carte[i][j] == 1: ligne += '#'
#             else: ligne += 'o'
#         print(ligne)

def onestep(carte,xs,ys):
    if carte[ys+1][xs] == 0: return xs,ys+1
    elif carte[ys+1][xs-1] == 0: return xs-1,ys+1
    elif carte[ys+1][xs+1] == 0: return xs+1,ys+1

def blocked(carte,xs,ys):
    return carte[ys+1][xs] != 0 and carte[ys+1][xs-1] != 0 and carte[ys+1][xs+1] != 0

def out(carte,ys):
    return ys >= ymax

## Chute du sable
compteur = 0
while True:
    xs,ys = xsource,ysource
    while not blocked(carte,xs,ys) and not out(carte,ys):
        xs, ys = onestep(carte,xs,ys)
    if out(carte,ys):
        break
    if blocked(carte,xs,ys):
        compteur += 1
    carte[ys][xs] = -1

print(compteur)


