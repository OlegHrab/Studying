#Олег Грабчак ТР-14 2023
yn    ='y'#присвоюємо...
emp   =0
numand=0
numz  =0
numsz =0
while yn=='y':#кожен раз якщо yn дорівнює символу 'y'
  print('do you want more?(y/n)')
  yn = input()#присвоїти yn введений символ/символи
  if yn=='y':#якщо yn дорівнює символу 'y'
     print('text filename:')
     #name = "text.txt"
     name = input()#вводимо назву файла 
     f1 = open(name,"r")#відкриваємо файл з іменем name на читання у змінну f1
     print(name)
     lines = f1.readlines()#прочитати рядки з файлу в lines
     print(lines)
     numstr = len(lines)#кількість елементів(рядків) множини lines
     for stri in lines:#цикл з кроками від першого(№0) до останнього рядка lines
         print(stri)
         if len(stri)==1:#якщо рядок пустий(тільки перевід рядка)
            emp=emp+1
         else:
             #шукаємо z
             ind = stri.count('z')#функція count підраховує кількість конкретних символів у рядку
             numz = numz + ind
             if ind>0:
                numsz = numsz + 1#підрахунок речень до яких входить символ z
             #шукаємо and
             ind = stri.count('and')
             numand = numand + ind 
         #end if
     #end for
     print('strings: ',numstr)
     print('  empty: ',emp)
     print(' with z: ',numsz)
     print('      z: ',numz)
     print('    and: ',numand)
     f1.close()#закриваємо файл 
#end while
