#Олег Грабчак ТР-14 2023
from num2words import num2words#звертаємося до встановленого пакету

def convert(number: int):
    return num2words(number, lang='uk')
