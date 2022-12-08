def visible(L,i,j):
    c = 0
    n = len(L)
    m = len(L[0])
    h,b,g,d = True,True,True,True
    for k in range(i):
        if L[k][j] >= L[i][j]: h = False # obstruction par le haut
    for k in range(i+1,n):
        if L[k][j] >= L[i][j]: b = False # par le bas
    for l in range(j):
        if L[i][l] >= L[i][j]: g = False # par la gauche
    for l in range(j+1,m):
        if L[i][l] >= L[i][j]: d = False # par la droite

    return h or b or g or d


with open('input8','r') as f:
    L = []
    for ligne in f.read().splitlines():
        Lcourante = []
        for c in ligne:
            Lcourante.append(int(c))
        L.append(Lcourante)

    tot = 0
    n = len(L)
    m = len(L[0])
    for i in range(n):
        for j in range(m):
            if visible(L,i,j): tot += 1

print(tot)

#8b
def score(L,i,j):
    scoreG, scoreD, scoreB, scoreH = 1,1,1,1
    n, m = len(L), len(L[0])

    pos = i-1
    while pos > 0 and L[pos][j] < L[i][j]:
        scoreG += 1
        pos -= 1

    pos = i+1
    while pos < n-1 and L[pos][j] < L[i][j]:
        scoreD += 1
        pos += 1

    pos = j-1
    while pos > 0 and L[i][pos] < L[i][j]:
        scoreH += 1
        pos -= 1

    pos = j+1
    while pos < m-1 and L[i][pos] < L[i][j]:
        scoreB += 1
        pos += 1

    return scoreG*scoreD*scoreH*scoreB


with open('input8','r') as f:
    L = []
    for ligne in f.read().splitlines():
        Lcourante = []
        for c in ligne:
            Lcourante.append(int(c))
        L.append(Lcourante)

    max = 0
    n = len(L)
    m = len(L[0])
    for i in range(n):
        for j in range(m):
            if score(L,i,j) > max:
                max = score(L,i,j)

print(max)

