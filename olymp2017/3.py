def IsPrime(n):
    for i in range(2, n):
        if (n % i == 0) and (i!=1) and (i!=n):
            return False
    return True
print(IsPrime(int(input())))
