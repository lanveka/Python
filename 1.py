def rec(a, b):
    if a > b:
        print('Квадрат ',b,' на ', b)
        return rec(a-b,b) + rec(a,a)
    elif a <b:
        print('Квадрат ',a,' на ', a)
        return rec(b-a,a) + rec(b,b)
    else:
        return 1


count = 0
a = int(input('Введите сторону прямоугольника А : '))
b = int(input('Введите сторону прямоугольника В : '))
print("Количество квадратов = ", rec(a,b))