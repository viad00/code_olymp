# RZ2T(SAM)_8.py
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
a = list(map(int, input().split()))

counter_ros = 0
counter_vio = 0
ros = []
vio = []

for i in range(1, n+1):
    if a[i-1] == i % 2:
        if i % 2 == 0:
            ros.append(i-1)
            counter_ros += 1
        else:
            vio.append(i-1)
            counter_vio += 1
if counter_vio == counter_ros:
    print(counter_ros)
    for i in range(counter_ros):
        print(ros[i]+1, ' ', vio[i]+1)
else:
    print(-1)
# ------------------------------------------ #
