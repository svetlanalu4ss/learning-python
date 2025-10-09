#  Findet die größte von drei eingegebenen Zahlen.



def main():
    print("Größte von drei Zahlen")
    numbers = []

    for index in range(1, 4):
        raw_value = input(f"Zahl {index}: ")
        try:
            number = float(raw_value)
        except ValueError:
            print("Bitte nur Zahlen eingeben.")
            return
        numbers.append(number)

    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number

    print(f"Die größte Zahl ist: {largest}")


if __name__ == "__main__":
    main()

