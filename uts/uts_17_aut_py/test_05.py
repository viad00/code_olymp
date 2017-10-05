m = 1
count = 0
while count != 110:
    count = 0
    mas = {}
    for i in range(1, m+1):
        mass = {}
        for j in range(1, m+1):
            mass[j] = 0
        mas[i] = mass
    # Аалгоритм
    k = 1
    while k <= m:
        n = 1
        while n <= m:
            mas[k][n] = mas[n][k] + k
            mas[n][k] = mas[k][n] - n
            n = n + 1
        k = k + 1
    k = m
    while k >= 1:
        n = m
        while n >= 1:
            mas[k][n] = mas[k][n] - mas[n][k]
            n = n - 1
        k = k - 1
    # Пподсчёт
    for i in range(1, m+1):
        for j in range(1, m+1):
            if mas[i][j] > 6:
                count += 1
    m += 1
    print(count)
# Уурааа
print('При m = {0}, c = {1}'.format(m-1, count))
