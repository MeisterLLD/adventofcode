map = [ ]
for ligne in open('input12','r').read().splitlines():
    current_line = []
    for char in ligne:
        current_line.append(char)
    map.append(current_line)

n = len(map)
m = len(map[0])
for i in range(n):
    for j in range(m):
        if map[i][j] == 'S':
            start_i,start_j = i,j
        if map[i][j] == 'E':
            end_i,end_j = i,j



#print(crt)



