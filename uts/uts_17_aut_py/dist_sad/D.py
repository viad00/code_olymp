import sys
sys.stdin=open('die.in','r')
sys.stdout=open('die.out','w')
def d(a):
    a[0],a[1],a[4],a[5]=a[4],a[5],a[1],a[0]
    return a
def l(a):
    a[0],a[1],a[2],a[3]=a[3],a[2],a[0],a[1]
    return a
def r(a):
    a[0],a[1],a[2],a[3]=a[2],a[3],a[1],a[0]
    return a
def u(a):
    a[0],a[1],a[4],a[5]=a[5],a[4],a[0],a[1]
    return a
b=[[1, 6, 2, 5, 3, 4], [1, 6, 2, 5, 4, 3], [1, 6, 3, 4, 2, 5], [1, 6, 3, 4, 5, 2], [1, 6, 4, 3, 2, 5], [1, 6, 4, 3, 5, 2], [1, 6, 5, 2, 3, 4], [1, 6, 5, 2, 4, 3], [2, 5, 1, 6, 3, 4], [2, 5, 1, 6, 4, 3], [2, 5, 3, 4, 1, 6], [2, 5, 3, 4, 6, 1], [2, 5, 4, 3, 1, 6], [2, 5, 4, 3, 6, 1], [2, 5, 6, 1, 3, 4], [2, 5, 6, 1, 4, 3], [3, 4, 1, 6, 2, 5], [3, 4, 1, 6, 5, 2], [3, 4, 2, 5, 1, 6], [3, 4, 2, 5, 6, 1], [3, 4, 5, 2, 1, 6], [3, 4, 5, 2, 6, 1], [3, 4, 6, 1, 2, 5], [3, 4, 6, 1, 5, 2], [4, 3, 1, 6, 2, 5], [4, 3, 1, 6, 5, 2], [4, 3, 2, 5, 1, 6], [4, 3, 2, 5, 6, 1], [4, 3, 5, 2, 1, 6], [4, 3, 5, 2, 6, 1], [4, 3, 6, 1, 2, 5], [4, 3, 6, 1, 5, 2], [5, 2, 1, 6, 3, 4], [5, 2, 1, 6, 4, 3], [5, 2, 3, 4, 1, 6], [5, 2, 3, 4, 6, 1], [5, 2, 4, 3, 1, 6], [5, 2, 4, 3, 6, 1], [5, 2, 6, 1, 3, 4], [5, 2, 6, 1, 4, 3], [6, 1, 2, 5, 3, 4], [6, 1, 2, 5, 4, 3], [6, 1, 3, 4, 2, 5], [6, 1, 3, 4, 5, 2], [6, 1, 4, 3, 2, 5], [6, 1, 4, 3, 5, 2], [6, 1, 5, 2, 3, 4], [6, 1, 5, 2, 4, 3]]
s=input()
mans=10000000
bans=0
for j in b:
    x=0
    for i in s:
        if i=='D':
            j=d(j)
        elif i=='L':
            j=l(j)
        elif i=='R':
            j=r(j)
        else:
            j=u(j)
        x+=j[0]
    if x>bans:
        bans=x+0
    if x<mans:
        mans=x+0
print(mans,bans)
