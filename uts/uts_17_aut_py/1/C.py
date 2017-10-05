n = int(input())


def conNS(x, si1 ,si2):
    x = int(str(x), si1)
    b = ''
    while x > 0:
        b, x = str(x%si2)+b, x//si2
    return b

n = conNS(n, 5, 7)
n = sum(list(map(int, str(n))))
n = conNS(n, 10, 3)
print(n)
