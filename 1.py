with open('input','r') as f:
    max = 0
    courant = 0
    for ligne in f.readlines():
        if ligne != '\n':
            L = ligne.split('\n')[0]
            cal = int(L)
            courant += cal
        else:
            if courant > max:
                max = courant
                print('reset')
            courant  = 0

print(max)
