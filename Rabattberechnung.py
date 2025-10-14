#Rabattberechnung
#Aufgabe:
#Schreibe ein Programm, das den Preis eines Produkts überprüft und 
# basierend auf dem Preis einen Rabatt gewährt:
#Für Produkte, die weniger als 50 Euro kosten, gibt es keinen Rabatt.
#Für Produkte, die zwischen 50 und 100 Euro kosten, gibt es einen Rabatt von 10%.
#Für Produkte, die mehr als 100 Euro kosten, gibt es einen Rabatt von 20%.
#Das Programm soll den Endpreis nach Abzug des Rabatts ausgeben.
#Beispiel:
 
#Gib den Preis des Produkts ein: 120
#Der Endpreis nach Rabatt ist 96.0 Euro.


preis = float (input ("Gib den Preis des Produkts ein:\n"))
if preis <=49:
    print ("Kein Rabbat. Dein Preis ist:", preis)
elif preis >=50 and preis <= 100:
    endpreis = preis - ((preis / 100) * 10)
    print ("Der Endpreis nach 10% Rabatt ist: ", endpreis)
elif preis >=101:
    endpreis = preis - ((preis / 100) * 20)
    print ("Der Endpreis nach 20% Rabatt ist: ", endpreis)