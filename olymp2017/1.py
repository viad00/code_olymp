def SumRange(a, b):
    sum = 0
    for i in range(a, b):
        sum += i
    sum += b
    return sum
a, b = list(map(int, input().split()))
print(SumRange(a, b))
