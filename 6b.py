#N = 4
N = 14


with open('input6','r') as f:
    b = f.read()

    set = {b[i] for i in range(N)}
    pos = N
    while len(set) < N:
        pos += 1
        set = {b[pos-N+i] for i in range(N) }
        print(set)
    print(pos)

