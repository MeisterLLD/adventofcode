from math import inf
xmin,ymin = inf,0
xmax,ymax = 0,0

xsource,ysource = 500,0

with open('input14','r') as fic:
    for ligne in fic.read().splitlines():
        path = ligne.split(' -> ')
        for s in path:
            x,y = s.split(',')
            x,y = int(x), int(y)
            if x > xmax:
                xmax = x
            if x < xmin:
                xmin = x
            if y > ymax:
                ymax = y

n = ymax+1
m = xmax+1

# Fabrication de la map
map = [ [0 for j in range(m)] for i in range(n+1) ]
map[ysource][xsource] = '+'

with open('input14','r') as fic:
    for ligne in fic.read().splitlines():
        path = ligne.split(' -> ')
        for i in range(len(path)-1):
            xdeb,ydeb = path[i].split(',')
            xdeb,ydeb = int(xdeb), int(ydeb)
            xfin,yfin = path[i+1].split(',')
            xfin,yfin = int(xfin), int(yfin)

            if xfin != xdeb:
                if xfin>= xdeb:
                    for j in range(xdeb,xfin+1):
                        map[ydeb][j] = 1
                else:
                    for j in range(xfin,xdeb+1):
                        map[ydeb][j] = 1

            elif yfin != ydeb:
                if yfin >= ydeb:
                    for k in range(ydeb,yfin+1):
                        map[k][xdeb] = 1
                else:
                    for k in range(yfin,ydeb+1):
                        map[k][xdeb] = 1


# Affichage
def affiche(map):
    for i in range(0,ymax):
        ligne = ''
        for j in range(xmin,xmax):
            if map[i][j] == '+': ligne += '+'
            elif map[i][j] == 0: ligne += '.'
            elif map[i][j] == 1: ligne += '#'
            else: ligne += 'o'
        print(ligne)



def onestep(map,xs,ys):
    if map[ys+1][xs] == 0: return xs,ys+1
    elif map[ys+1][xs-1] == 0: return xs-1,ys+1
    elif map[ys+1][xs+1] == 0: return xs+1,ys+1

def blocked(map,xs,ys):
    return map[ys+1][xs] != 0 and xs-1>=xmin-1 and map[ys+1][xs-1] != 0 and xs+1<=xmax and map[ys+1][xs+1] != 0

def out(map,ys):
    return ys >= ymax

# Chute du sable
compteur = 0
while True:
    xs,ys = xsource,ysource
    while not blocked(map,xs,ys) and not out(map,ys):
        xs, ys = onestep(map,xs,ys)
    if out(map,ys):
        break
    if blocked(map,xs,ys):
        compteur += 1

    map[ys][xs] = -1

affiche(map)
print(compteur)


