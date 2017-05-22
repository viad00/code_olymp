def fun(s):
    sum = 0
    ff = len(s)
    for i in range(ff):
        sum += int(s[i])
    return sum
print(fun(str(input())))
