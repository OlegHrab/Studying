from .number_to_words import convert

def main():

    number = int(input("Введіть число: "))
    words = number_to_words.convert(number)
    print(f"Ви ввели: {words}")
