n = int(input())  # Unfinished
mas = input().split()
cnt = 0
for i in range(n):
    curstr = str(*mas[:n] + mas[n:])
    if curstr == curstr[::-1]:
        cnt += 1
print(cnt)
