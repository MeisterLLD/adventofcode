def scoresymb(c):
    if c == 'X': return 1
    if c == 'Y': return 2
    if c == 'Z': return 3

def scorecomb(c1,c2):
    d1 = c1
    if c2 == 'X':
        d2 = 'A'
    elif c2 == 'Y':
        d2 = 'B'
    else:
        d2 = 'C'

    if d2 == d1:
        return 3
    if (d2 > d1 and not(d2 == 'C' and d1 =='A')) or (d2 == 'A' and d1 =='C'):
        return 6
    else:
        return 0


score = 0
with open('input2','r') as f:
    for ligne in f.read().splitlines():
        print(ligne)
        s1, s2 = ligne.split(' ')
        score += scoresymb(s2) + scorecomb(s1,s2)

print(score)

