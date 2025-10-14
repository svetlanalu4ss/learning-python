#Aufgabe 2: Taschenrechner (mit if/else)
#Aufgabe:
#Schreibe ein Programm, das einen einfachen Taschenrechner simuliert. 
# Der Benutzer gibt zwei Zahlen und einen Operator (z.B. +, -, *, /) ein. 
# Das Programm soll den entsprechenden Rechenvorgang ausführen und das Ergebnis ausgeben. 
# Bei ungültigen Operatoren oder einer Division durch Null soll eine entsprechende Fehlermeldung angezeigt werden.
#Beispiel:
 
#Gib die erste Zahl ein: 10
#Gib den Operator ein (+, -, *, /): /
#Gib die zweite Zahl ein: 2
#Ergebnis: 5.0
#Bei ungültigem Operator:
 
#Ungültiger Operator! Bitte gib einen gültigen Operator ein (+, -, *, /).
#Bei Division durch Null:
#Fehler: Division durch Null ist nicht erlaubt.

print("Einfacher Taschenrechner")  # Заголовок программы
# Ввод чисел пользователем
first_input = input("Erste Zahl: ")   # Получаем первую цифру
second_input = input("Zweite Zahl: ") # Получаем вторую цифру

# Преобразуем текст в число
number1 = float(first_input)  # float() превращает текст в число с запятой
number2 = float(second_input)

# Ввод операции
operation = input("Operation (+, -, *, /): ")  # +, -, *, /

# Проверяем каждую операцию отдельно
if operation == "+":
    print("Ergebnis:", number1 + number2)  # Сложение
elif operation == "-":
    print("Ergebnis:", number1 - number2)  # Вычитание
elif operation == "*":
    print("Ergebnis:", number1 * number2)  # Умножение
elif operation == "/":
    if number2 == 0:                       # Проверка деления на ноль
        print("Division durch Null ist nicht erlaubt.")  # Вывод предупреждения
    else:
        print("Ergebnis:", number1 / number2)  # Деление
else:
    print("Unbekannte Operation.")          # Если операция не известна
    
    
    
    
# ========================================================
# 🔹 Простой калькулятор для новичка
# ========================================================

print("Einfacher Taschenrechner")  # Заголовок

# Ввод чисел пользователем
first_input = input("Erste Zahl: ")   # Получаем первую цифру
second_input = input("Zweite Zahl: ") # Получаем вторую цифру

# Преобразуем текст в число
number1 = float(first_input)  # float() превращает текст в число с запятой
number2 = float(second_input)

# Ввод операции
operation = input("Operation (+, -, *, /): ")

# Проверяем, какая операция выбрана
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number2 == 0:  # проверка деления на ноль
        print("Division durch Null ist nicht erlaubt.")
    else:
        result = number1 / number2
else:
    print("Unbekannte Operation.")

# Вывод результата (если операция была правильная)
if operation in ["+", "-", "*", "/"] and not (operation == "/" and number2 == 0):
    print("Ergebnis:", result)  # Вывод числа вместе с текстом














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
