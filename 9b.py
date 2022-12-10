def norm(dx,dy):
    return abs(dx) + abs(dy)

def movetail(head,tail):
    x,y = head
    x2,y2 = tail
    dx,dy = x-x2, y-y2

    if norm(dx,dy) <= 1: return tail

    if norm(dx,dy) == 2:
        if dx==0 or dy==0: return (x2+dx//2, y2+dy//2)
        else: return tail

    if norm(dx,dy) == 3:
        if abs(dy) == 2:
            x2 = x
            y2 = y2 + dy//2
        else:
            x2 = x2 + dx//2
            y2 = y
        return x2,y2

    # Sinon on est à distance 4
    return (x2+dx//2, y2+dy//2)



dicdir = {'L':(-1,0), 'R':(1,0), 'U':(0,1), 'D':(0,-1)  }
rope = [(0,0)]*10
postail = {(0,0)}

with open('input9','r') as f:
    for ligne in f.readlines():
        dir = dicdir[ligne.split(' ')[0]]
        nb = int(ligne.split(' ')[1])

        for i in range(nb):
            head = rope[0]
            rope[0] = (head[0]+dir[0], head[1]+dir[1])
            for i in range(1,10):
                rope[i] = movetail(rope[i-1],rope[i])
            postail.add( rope[-1]  )

print(len(postail))

