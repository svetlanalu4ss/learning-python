a = int(input("Bitte gib das Seite a ein: "))   # input() — спрашивает ввод с клавиатуры; int() — превращает введённое число из текста в целое число
b = int(input("Bitte gib das Seite b ein: "))
c = int(input("Bitte gib das Seite c ein: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Seitenlängen müssen positiv sein")

elif not (a + b > c and a + c > b and b + c > a):
    print("Kein gültiges Dreieck.")
elif a == b == c:                 
    print("Das Dreieck ist gleichseitig.") 
elif  a == b or a == c or b == c:               
    print("Das Dreieck ist Gleichschenklig.")  # равнобедренный
