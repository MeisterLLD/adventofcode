def win(c):
    if c == 'A': return 'B'
    if c == 'B': return 'C'
    if c == 'C': return 'A'

def lose(c):
    if c == 'A': return 'C'
    if c == 'B': return 'A'
    if c == 'C': return 'B'

def decide(c1,c2):
    if c2 == 'X': return lose(c1)
    if c2 == 'Y': return c1
    if c2 == 'Z': return win(c1)


def scoresymb(c):
    if c == 'A': return 1
    if c == 'B': return 2
    if c == 'C': return 3

def scorecomb(d1,d2):
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
        s2 = decide(s1,s2)
        score += scoresymb(s2) + scorecomb(s1,s2)

print(score)

