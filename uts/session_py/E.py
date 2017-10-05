import sys
problem_name = str('input')
sys.stdout = open("output.txt", "w")
def unff(number, arr, base):
    res = ""
    while number > 0:
        y = arr[number % base]
        res = y + res
        number = int(number // base)
    return res
dec_mas = []
arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
f = open(problem_name + ".txt")
s = []
for line in f:
    s.append(line)
for od in range(1, len(s)):
    dec_mas.append(int(s[od]))
b = int(s[0])
count = {}
count = {i: 0 for i in arr}
for i in dec_mas:
    un = unff(i, arr, b)
    s = []
    for o in un:
        if not(o in s):
            count[o] += 1
            s.append(o)
maxim = 0
index = 0
for i in count:
    if count[i] > maxim:
        maxim = count[i]
        index = i
print(index)
