with open('input4','r') as f:
    tot = 0
    for ligne in f.readlines():
        r1,r2 = ligne.split(',')[0], ligne.split(',')[1]
        d1,f1 = int(r1.split('-')[0]), int(r1.split('-')[1])
        d2,f2 = int(r2.split('-')[0]), int(r2.split('-')[1])

        if d2 >= d1 and f2 <= f1 or d1 >= d2 and f1 <= f2:
            tot += 1
            print(d1,f1,' --- ', d2,f2)

print(tot)
