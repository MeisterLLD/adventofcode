items = [[61], [76, 92, 53, 93, 79, 86, 81], [91, 99], [58, 67, 66], [94, 54, 62, 73], [59, 95, 51, 58, 58], [87, 69, 92, 56, 91, 93, 88, 73], [71, 57, 86, 67, 96, 95]]
inspected = [0]*8

from math import floor, lcm

def operation(i, x):
    if i == 0: return x*11
    if i == 1: return x+4
    if i == 2: return x*19
    if i == 3: return x*x
    if i == 4: return x+1
    if i == 5: return x+3
    if i == 6: return x+8
    if i == 7: return x+7

def relief(i, x):
    return floor(x/3)

def test(i, x):
    if i == 0: return x%5 == 0
    if i == 1: return x%2 == 0
    if i == 2: return x%13 == 0
    if i == 3: return x%7 == 0
    if i == 4: return x%19 == 0
    if i == 5: return x%11 == 0
    if i == 6: return x%3 == 0
    if i == 7: return x%17 == 0

def sendto(i,bool):
    if i == 0: return 7 if bool else 4
    if i == 1: return 2 if bool else 6
    if i == 2: return 5 if bool else 0
    if i == 3: return 6 if bool else 1
    if i == 4: return 3 if bool else 7
    if i == 5: return 0 if bool else 4
    if i == 6: return 5 if bool else 2
    if i == 7: return 3 if bool else 1

def manage(y):
    return y % lcm(5,2,13,7,19,11,3,17)

tour = 0
while(tour < 10000):
    for i in range(8):
        nbitems = len(items[i])
        for _ in range(nbitems):
            x = items[i].pop(0)
            y = operation(i, x)
            z = manage(y)def dijkstra2(g, source, arrivee):
    ''' Dijkstra qui s'arrête dès qu'on tombe sur arrivee,
    renvoie la distance et un chemin optimal
    Entrée : un dictionnaire d'adjacence pondéré g. Chaque
    objet est une liste de tuples.
    Par ex g[0] = [(1,85), (2, 217), (4,173) ] etc.
    '''
    dist = { } # dictionnaire des distances à source
    peres = { } # dictionnaire des pères
    for s in g:
        dist[s] = inf
    dist[source] = 0
    V = set()
    V.add(source)
    while len(V) > 0:
        # recherche de la priorité maximale dans V
        cand = None
        mini = inf
        for s in V:
            if dist[s] < mini:
                mini = dist[s]
                cand = s
        if cand == arrivee: break
        V.remove(cand)
        print('En train de traiter', cand)
        # le prochain sommet traité est cand(idat)
        for (v, d) in g[cand]: # on parcourt les voisins
            if dist[cand] + d < dist[v]:
                V.add(v)
                dist[v] = dist[cand] + d
                peres[v] = cand

    # Reconstitution du chemin de source à arrivee
    c = arrivee
    chemin = [c]
    while c != source:
        c = peres[c]
        chemin.append(c)

    return dist[arrivee], chemin

G = {0:[(1,85),(2,217),(4,173) ], 1:[(0,85), (5,80)], 2:[(0,217), (6,186),(7,103)  ], 3:[(7,183)], 4:[(0,173), (9,502) ], 5:[(1,80), (8,250)   ], 6:[(2,186)   ], 7:[(2,103),(3,183),(9,167) ], 8:[(5,250),(9,84)   ], 9:[(8,84),(7,167),(4,502)   ]}

print(dijkstra2(G,0,9))
            inspected[i] += 1
            dest = sendto(i, test(i,z))
            items[dest].append(z)
    tour += 1

inspected.sort()
print(inspected[-1]*inspected[-2])







