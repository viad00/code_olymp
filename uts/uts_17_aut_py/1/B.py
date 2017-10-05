n = int(input())
lastnum = n
otv = ''
print(1, end=' ')
while lastnum <= 10**9 and lastnum > 1:
    print(lastnum, end=' ')
    lastnum = lastnum * n
