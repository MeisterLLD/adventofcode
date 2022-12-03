def prio(c):
    if c > 'Z':
        return ord(c)-96
    else:
        return ord(c)-64+26

tot = 0
ligne1 = 'I love Paul McCartney'
with open('input3','r') as f:
    while ligne1 != '':
        ligne1 = f.readline()
        ligne2 = f.readline()
        ligne3 = f.readline()
        for c in ligne1:
            if c in ligne2 and c in ligne3:
                tot += prio(c)
                break

print(tot)