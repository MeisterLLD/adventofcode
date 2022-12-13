import ast

def lexavant(a,b):

    if a == [] and b == []: return None

    if type(a)==int and type(b)==int:
        if a<b: return True
        if a>b: return False

    if type(a)==list and type(b)==list:
        if len(a) == 0 and len(b)>0: return True
        if len(a)>0 and len(b)==0: return False

    if type(a) == list and type(b) == list:
        a0, b0 = a[0], b[0]
        if type(a0) == int and type(b0) == list:
            a0 = [a0]
            lexavant(a0,b0)
        if type(a0) == list and type(b0) == int:
            b0 = [b0]
            lexavant(a0,b0)
        if lexavant(a0,b0)!=None: return lexavant(a0,b0)
        else: return lexavant(a[1::],b[1::])

tot = 0
with open('input13','r') as f:
    i = 1
    while True:
        a = f.readline()
        if a == '': break
        a = ast.literal_eval(a)
        b = ast.literal_eval(f.readline())
        if lexavant(a,b):
            tot += i
        f.readline()
        i += 1

print(tot)


#13b
sorted = []
with open('input13','r') as f:
    while True:
        a = f.readline()
        if a == '': break
        a = ast.literal_eval(a)
        sorted.append(a)
        b = ast.literal_eval(f.readline())
        sorted.append(b)
        f.readline()
    sorted.append([[2]])
    sorted.append([[6]])


def triins(tab):
    for i in range(1,len(tab)):
        clé = tab[i]
        j = i
        while j > 0 and  lexavant(clé,tab[j-1]):
            tab[j-1], tab[j] = tab[j], tab[j-1]
            j = j - 1
    return tab

triins(sorted)

for i in range(len(sorted)):
    if sorted[i] == [[2]]: a = i+1
    if sorted[i] == [[6]]: b = i+1

print(a*b)

