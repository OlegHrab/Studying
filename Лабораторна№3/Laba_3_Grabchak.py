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
