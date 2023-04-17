#Олег Грабчак ТР-14 2023
from num2words import num2words

def convert(number: int) -> str:
    return num2words(number, lang='en')
