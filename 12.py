map = [ ]
for ligne in open('input12','r').read().splitlines():
    current_line = []
    for char in ligne:
        current_line.append(char)
    map.append(current_line)


n = len(map)
m = len(map[0])

def ord2(c):
    if c=='S': return 97
    if c=='E': return 122
    return ord(c)


def voisins(coord):
    i,j = coord
    pot = [ (i-1,j), (i+1,j), (i,j-1), (i,j+1)    ]
    return [ (x,y) for (x,y) in pot if x>=0 and y>=0 and x<n and y<m and ord2(map[x][y]) <= ord2(map[i][j])+1   ]

for i in range(n):
    for j in range(m):
        if map[i][j] == 'S':
            start = i,j
        if map[i][j] == 'E':
            end = i,j


def distlarg(root):
    vus = {root}
    dist = { }
    file = [root]
    dist[root] = 0

    while len(file)>0:
        cour = file.pop(0)  # on défile (à gauche, donc)
        for s in voisins(cour):  # pour tous les voisins de cour (le défilé)
            if s not in vus:
                vus.add(s)
                file.append(s)  #on l'a vu et on l'enfile
                dist[s]=dist[cour]+1

    return dist


dist = distlarg(start)
print(dist[end])

#12b
starts = []
for i in range(n):
    for j in range(m):
        if map[i][j] == 'a' or map[i][j] == 'S': starts.append((i,j))

from math import inf
min = inf
for s in starts:
    if end in distlarg(s):
        d = distlarg(s)[end]
        if d < min:
            min = d
print(min)
