import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

test_num = int(input())
for test in range(test_num):
    b = 'NO'
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        b = 'YES'
    elif n == 2:
        b = 'NO'
    else:
        left = 0
        right = sum(a[1:])
        for i in range(1, n-1):
            left += a[i - 1]
            right -= a[i]
            if left == right:
                b = 'YES'
                break
    print(b)