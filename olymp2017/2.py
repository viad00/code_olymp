def Calc(a, b, op):
    dived = {
        1: a-b,
        2: a*b,
        3: a/b,
        }
    try:
        return dived[op]
    except KeyError:
        return a+b
a, b, op = list(map(int, input().split()))
print(Calc(a, b, op))
