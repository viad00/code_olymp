oldn = 2
s = 0
while s != 3203:
    n = oldn
    i = 2
    s = 0
    c = 0
    while n != 1:
        if n % i==0:
            n = n // i
            c = c +1
        else:
            s = s * 10 + c
            c = 0
            i = i + 1
    s = s * 10 + c
    s = s
    oldn += 1

print(oldn-1)
