a, b, d = list(map(int, input().split()))

if a < b:
    if a + d >= b:
        print(b)
    elif a + d < b:
        print(a+d)
elif a > b:
    if a - d <= b:
        print(b)
    elif a - d > b:
        print(a-d)
else:
    print(b)
