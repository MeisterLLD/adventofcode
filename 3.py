def prio(c):
    if c > 'Z':
        return ord(c)-96
    else:
        return ord(c)-64+26

tot = 0
with open('input3','r') as f:
    for ligne in f.read().split('\n'):
        N = len(ligne)
        ligne1 = ligne[0:N//2]
        ligne2 = ligne[N//2:]
        print(ligne1, '-', ligne2)
        for c in ligne1:
            if c in ligne2:
                print(c)
                tot += prio(c)
                break
print(tot)