celsius = float(input("Gib die Temperatur in °C ein: "))

fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15

print(f"Fahrenheit: {fahrenheit} °F")
print(f"Kelvin: {kelvin} K")

if celsius < 0:
    print("Hinweis: Die Temperatur liegt unter dem Gefrierpunkt.")
