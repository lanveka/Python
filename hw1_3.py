# задание 3 вариант №4 "Найти значение минимального элемента списка"
import random
#ввод
n = int(input("list:\n"))
A = []
for i in range(n):
    a = random.randint(0,99)
    A.append(a)
    print(A[i])

minimum = A[0]
for i in range(n):
    if A[i] < minimum:
        minimum = A[i]
print("Минимальное число:", minimum)




