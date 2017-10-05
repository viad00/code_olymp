ser = int(input())
mas = list(map(int, input().split()))
ind = ser // 2
mas1 = mas[:ind]
mas2 = mas[ind:]
mas1.sort()
mas2.sort(reverse=True)
for i in mas1:
    print(i, end=' ')
for i in mas2:
    print(i, end=' ')
