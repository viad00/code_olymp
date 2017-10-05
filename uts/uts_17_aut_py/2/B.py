ser = int(input())
mas = list(map(int, input().split()))
cnt = 0
for i in range(ser):
    srav = mas[i]
    for j in range(i, ser):
        if srav > mas[j]:
            cnt += 1
print(cnt)
