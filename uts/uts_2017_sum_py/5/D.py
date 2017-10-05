import sys

sys.stdin = open('robot.in', 'r')
s = input()

d = 0
a = []
f = 0
c = 0
x = 0
y = 0
for i in s:
    if i == 'S':
        if (x, y) in a:
            print(c)
            exit()
        a.append((x, y))
        c += 1
        if d == 0:
            x += 1
        if d == 1:
            y += 1
        if d == 2:
            x -= 1
        if d == 3:
            y -= 1
    if i == 'L':
        d = (d + 1) % 4
    if i == 'R':
        d = (d - 1) % 4
if (x, y) in a:
    print(c)
else:
    print(-1)
