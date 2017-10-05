def swi(g):
    if g == 1:
        return 0, False
    if g == 0:
        return 1, True
a = input()
b = input()
ex = []
g = 0
for i in b:
    g, doo = swi(g)
    if (doo) and (not (i in ex)):
        ex.append(i)
b = ''
for i in a:
    if not (i in ex):
        b += i
print(b)