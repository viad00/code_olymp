from collections import Counter
n = int(input())
mas = list(map(int, input().split()))
print(Counter(mas).most_common()[0][0])
