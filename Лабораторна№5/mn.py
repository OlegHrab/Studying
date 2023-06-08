#Олег Грабчак ТР-14 2023
from mp import number_to_words#підключаємо скрипт number_to_words із каталога mp

def m_n():
    number=1
    while number!=0:#поки number не дорівнює нулю
      number = int(input("Введіть номер: "))#вводимо символи і конвертуємо їх в цілі числа
      words = number_to_words.convert(number)#викликаємо функцію convert зі скрипта number_to_words
      print(f"Ви ввели: {words}")#вивід змінної words з форматуванням
     
    #while
    #m_n()
m_n()#виклик функції
  
