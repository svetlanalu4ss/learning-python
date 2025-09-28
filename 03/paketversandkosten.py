basispreis = 5.0
preis_pro_kg = 2.0
preis_pro_km = 0.01

gewicht = float(input("Gib das Gewicht des Pakets in kg ein: "))
entfernung = float(input("Gib die Entfernung in km ein: "))

kosten = basispreis + gewicht * preis_pro_kg + entfernung * preis_pro_km
print(f"Versandkosten: {kosten} €")

if gewicht > 20:
    print("Achtung: Das Paket gilt als Sperrgut.")
