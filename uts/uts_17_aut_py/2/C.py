ser = int(input())
ner = list(map(int, input().split()))
ner.sort()
if ser % 2 != 0:
    print(ner[ser // 2])
else:
    ma = (ser // 2) - 1
    mi = (ser // 2)
    lg = ner[mi] + ner[ma]
    kek = lg / 2
    print(kek)
