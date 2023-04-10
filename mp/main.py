from mp import number_to_words

def mn():

    number = int(input("Введіть число: "))
    words = number_to_words.convert(number)
    print(f"Ви ввели: {words}")


if __name__ == "__main__":
    mn()