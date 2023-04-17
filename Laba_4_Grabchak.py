#Олег Грабчак ТР-14 2023
yn    ='y'
emp   =0
numand=0
numz  =0
numsz =0
while yn=='y':
  print('do you want more?(y/n)')
  yn = input()
  if yn=='y':
     print('text filename:')
     #name = "text.txt"
     name = input()
     f1 = open(name,"r")
     print(name)
     lines = f1.readlines()
     print(lines)
     numstr = len(lines)
     for stri in lines:
         print(stri)
         if len(stri)==1:
            emp=emp+1
         else:
             #шукаємо z
             ind = stri.count('z')
             numz = numz + ind
             if ind>0:
                numsz = numsz + 1 
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
     f1.close()  
#end while
