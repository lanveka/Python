import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика

def ShakerSort(A): # Функция шейкерной (коктейльной) сортировки shaker
   for i in range(0, int(N/2)):
       for j in range(i, N-1-i):
           if A[j] > A[j+1]:
               a = A[j]
               A[j] = A[j + 1]
               A[j + 1] = a
       for j in range (len(A), N-2, i+1):
           if A[j] < A[j-1]:
               a = A[j]
               A[j] = A[j - 1]
               A[j - 1] = a



def QuickSort(A, fst, lst):         # быстрая сортировка
    if fst >= lst:
        return

    #i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst+1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger+1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger-1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller-1)
    QuickSort(A, first_bigger, lst)


table = prettytable.PrettyTable(["Размер списка", "Время shakersort", "Время быстрой"])
x=[]
y1=[]
y2=[]



for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    #print(A)

    B = A.copy()
    # print(B)

    # ShakerSort(A)
    print("---")
    # print(A)


    # QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    ShakerSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Shaker   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B)-1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)

plt.plot(x, y1, "#00FF00")
plt.plot(x, y2, "C1")
plt.show()