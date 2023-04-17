# Studying
#Олег Грабчак ТР-14 2023
def mum(parameters):#визначаю функцію у яку можна ввести парвметр   
    if parameters:#якщо parameters надано значення
       print(parameters)
       numbers=parameters
       indexout=[]#привласнюю змінній indexout порожній набір
       llen=len(numbers)#отримую кількість елементів у numbers в llen
       for i in range(llen):#цикл з кроками від i=0 до значення llen
           if not(i in indexout):#якщо значення i у цій ітерації НЕ є вже у множині(наборі) indexout
              indexout.append(i)#додати до набору indexout значення i у цій ітерації
              for j in range(i+1,llen):#цикл з кроками від j=i+1 до значення llen
                  if not(j in indexout):#якщо значення j у цій ітерації НЕ є вже у множині(наборі) indexout
                     if int(numbers[i])+int(numbers[j])==10:#функція int(змінна) перетворює символ у ціле число
                        indexout.append(j)#додати до набору indexout значення j у цій ітерації
                        print(numbers[i],"+",numbers[j],"=10")
                        break#завершення блоку порівняння
if __name__ == '__main__':#умова if __name__ == '__main__' перевіряє, чи був файл запущений безпосередньо
 import sys#модуль sys надає доступ до системних функцій та змінних
 mum(sys.argv[1:])#скрипт який передає параметри із командного рядка при запуску в задану функцію 



# Результати роботи програми
# Запуск у середовищі IDLE (Python 3.11 64-bit), пункт меню run customized
===================== RESTART: D:\p_labs\Laba_3_Grabchak.py ====================

['1', '3', '4', '2', '5', '6', '7', '8', '9', '6', '0', '5', '4', '5']

1 + 9 =10

3 + 7 =10

4 + 6 =10

2 + 8 =10

5 + 5 =10

6 + 4 =10


# Запуск у cmd.exe
C:\Users\olegh\AppData\Local\Programs\Python\Python311>python Laba_3_Grabchak.py 1 9 2 8 7 3 4 5 0 4 5 0

['1', '9', '2', '8', '7', '3', '4', '5', '0', '4', '5', '0']

1 + 9 =10

2 + 8 =10

7 + 3 =10

5 + 5 =10
