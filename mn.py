from mp import number_to_words

def m_n():
    number=1
    while number!=0:
      number = int(input("Введіть номер: "))
      words = number_to_words.convert(number)
      print(f"Ви ввели: {words}")
     
    #while
    #m_n()
m_n()
  