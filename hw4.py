#Скопировать в файл F2 только те строки из F1,
# которые начинаются с буквы «А». Подсчитать количество слов в F2.
with open("f1.txt", encoding="utf8") as file:
    line = file.readlines()
    print(line)
result = []
for i in line:
    if i[0].lower() == 'а' :
         result.append(i)
print(result)
f = open('f2.txt', 'w')

# 8. Цикл записи каждой строки списка в файл
for i in result:
    f.write(i)

# 9. Закрыть файл
f.close()
# 2.1. Открыть текстовый файл для чтения
c = open('f2.txt', 'r')

# 2.2. Прочитать строки файла в список L
L = c.readlines()

# 2.3. Количество элементов списка == количество строк в файле
count = len(L)
print('count = ', count)

# 2.4. Закрыть файл
c.close()