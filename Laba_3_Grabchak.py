#Олег Грабчак ТР-14 2023
def mum(parameters):
    if parameters:
       print(parameters)
       numbers=parameters
       indexout=[]
       llen=len(numbers)
       for i in range(llen):
           if not(i in indexout):
              indexout.append(i)
              for j in range(i+1,llen):
                  if not(j in indexout):
                     if int(numbers[i])+int(numbers[j])==10:
                        indexout.append(j)
                        print(numbers[i],"+",numbers[j],"=10")
                        break
if __name__ == '__main__':
 import sys
 mum(sys.argv[1:])
