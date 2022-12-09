def dist(head,tail):
    xh,yh = head
    xt,yt = tail
    return abs(xt-xh)+abs(yt-yh)

def movetail(dir,head,tail):
    x,y = head
    dx,dy = dir

    x2,y2 = tail

    if dist(head,tail) <= 1: return tail

    if dist(head,tail) == 2:
        if x==x2 or y==y2: return (x2+dx, y2+dy)
        else: return tail


    # on est à distance 3
    if abs(y-y2) == 2:
        x2 = x
        y2 = y2 + dy
    else:
        x2 = x2 + dx
        y2 = y
    return x2,y2





dicdir = {'L':(-1,0), 'R':(1,0), 'U':(0,1), 'D':(0,-1)  }

head = (0,0)
tail = (0,0)

postail = {tail}

with open('input9','r') as f:
    for ligne in f.readlines():
        dir = dicdir[ligne.split(' ')[0]]
        nb = int(ligne.split(' ')[1])


        for i in range(nb):
            head = (head[0]+dir[0], head[1]+dir[1])
            tail = movetail(dir,head,tail)
            postail.add( tail  )

print(len(postail))

