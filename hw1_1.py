# Задание 1 вариант 7 "В переменную Y ввести номер года. Определить, является ли год високосным."
y = int(input("Веедите год:\n"))
if y%400==0 :
    print('Високосный')
elif y%4 ==0 and y%100!=0:
    print(str(y)+' Високосный')
else:
    print('Обычный')