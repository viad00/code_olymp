import sys

ID = "strings"
sys.stdin = open(ID + ".in", "r")


# sys.stdout = open(ID + ".out", "w")

def KMP(s, x):
   S = x + '#' + s  # Большая строка
   print('S = ' + S)
   P = [0] * len(S)  # Префикс-функция
   m = len(x)  # Длина подстроки
   # print(template)
   found = False
   for i in range(1, len(S)):
       # Префикс-функция для предыдущего
       # символа
       # i - индекс в строке
       # j - индекс в префиксе (подстроке)
       print()
       print('Символ: ' + S[:i] + "[" + S[i] + "]" + S[(i + 1):], end='  ')
       j = P[i - 1]  # незачем смотреть всю строку, можно посмотреть со сдвига прошлой подстроки
       print('P[' + str(i - 1) + '] = ' + str(j), end=' ')
       while j > 0 and S[j] != S[i]:
           print('j: ' + str(j - 1) +
                 ' -> P[' + str(j - 1) + '] = '
                 + str(P[j - 1]), end=' ')
           j = P[j - 1]
       if S[j] == S[i]:
           j += 1
           print(' S[' + str(j) + '] == S[' + str(i) + '] == ' + str(S[i]) + '   ' +
                 'P[' + str(i) + '] = ' + str(j), end='  ')
       P[i] = j
       # Если видим длину подстроки
       # то мы её нашли
       if j == m:
           if found:
               print(' ', end='')
           found = True
           print(i - m * 2 + 1)
   if not found:
       print('none')
   print(P)


while True:
   try:
       s = input()
       t = input()
   except EOFError:
       break
   KMP(s, t)

sys.stdout.close()
