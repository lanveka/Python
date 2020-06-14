def rec(n, m):
    k = 1
    while n != m:
        if n > m:
            n -= m
        else:
            m -= n
        k += 1
    print('МОЖНО РАЗДЕЛИТЬ ПРЯМОУГОЛЬНИК НА ' + str(k) + ' КВАДРАТОВ')


n = int(input('Введите сторону прямоугольника А : '))
m = int(input('Введите сторону прямоугольника В : '))
print(rec(n, m))
