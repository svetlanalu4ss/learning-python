# Einfacher Taschenrechner: nimmt zwei Zahlen und eine Operation entgegen und gibt das Ergebnis aus.

def main():
    print("Einfacher Taschenrechner")
    first_input = input("Erste Zahl: ")
    second_input = input("Zweite Zahl: ")
    operation = input("Operation (+, -, *, /): ")

    try:
        number1 = float(first_input)
        number2 = float(second_input)
    except ValueError:
        print("Bitte nur Zahlen eingeben.")
        return

    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        if number2 == 0:
            print("Division durch Null ist nicht erlaubt.")
            return
        result = number1 / number2
    else:
        print("Unbekannte Operation.")
        return

    print(f"Ergebnis: {result}")


if __name__ == "__main__":
    main()
