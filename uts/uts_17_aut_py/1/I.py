ser = int(input())
mas = list(map(int, input().split()))
rem = mas[0]
mas.sort()
print(mas.index(rem) + 1)
