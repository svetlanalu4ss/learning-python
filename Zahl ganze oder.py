# Prüft, ob eine eingegebene Zahl gerade oder ungerade ist.

eingabee = float (input("Zahl:"))

if eingabee % 2 == 0: 
    print ("Gerade")
elif eingabee %2 ==1:
    print ("Ungerade")
else: 
    print ("weder noch")




def main():
    print("Gerade oder ungerade?")
    user_input = input("Bitte eine ganze Zahl eingeben: ")

    if not user_input.strip():
        print("Keine Eingabe erhalten.")
        return

    try:
        number = int(user_input)
    except ValueError:
        print("Bitte eine ganze Zahl eingeben.")
        return

    if number % 2 == 0:
        print(f"{number} ist gerade.")
    else:
        print(f"{number} ist ungerade.")


if __name__ == "__main__":
    main()
