le, de = list(map(int, input().split()))
de = bin(de)[2:]
if len(de) < le:
    de = ('0'*(le - len(de))) + de

print(de)
