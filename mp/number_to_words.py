from num2words import num2words

def convert(number: int) -> str:
    return num2words(number, lang='en')