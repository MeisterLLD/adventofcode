with open('input','r') as f:
    liste = []
    courant = 0
    for ligne in f.readlines():
        if ligne != '\n':
            L = ligne.split('\n')[0]
            cal = int(L)
            courant += cal
        else:
            liste.append(courant)
            courant  = 0

liste.sort()
print(liste[-1]+liste[-2]+liste[-3])