#N = 4
N = 14


with open('input6','r') as f:
    b = f.read()
    dic = {}
    for i in range(N):
        if b[i] not in dic: dic[b[i]] = 1
        else: dic[b[i]] += 1



    pos = N-1
    while len(dic) < N:
        pos += 1
        new = b[pos]
        old = b[pos-N]

        if old in dic:
            if dic[old] == 1: dic.pop(old)
            else: dic[old] -= 1

        if new not in dic: dic[new] = 1
        else: dic[new] += 1


    print(pos+1)
