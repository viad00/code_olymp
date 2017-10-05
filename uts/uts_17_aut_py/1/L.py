ser = int(input())
mas = list(map(int, input().split()))
kek = 0
while True:
    if kek in mas:
        kek += 1
    else:
        print(kek)
        break
