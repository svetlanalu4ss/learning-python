# Aufgabe: Altersprufung fur Mofa, Moped und Auto
# Mofa: ab 14
# Moped: ab 16
#Auto: ab 18
# Eingabe, die ganzzahlige weertee annimt und dann ausgibt von 0 bis 89,
#welche Fahrzeug (Mofa,Moped oder Auto) empfolen wird
#wenn die Eingabe nicht ganzzahlig ist,oder unter null, soll eine entsprechende Fehlermeldung ausgegeben weerden

alter = int (input ("Wie alt bist du?\n Ich bin: "))
if alter <= 0 or alter % 1 != 0:
    print ("Eingabe inkorrekt")
if alter >= 0 and alter <= 13:
    print ("Leider, du darfst nicht Fahrzeug benutzen")
if alter >= 89:
    print ("Leider, es ist zu spat")
if alter >= 14 and alter <= 15:
    print ("Im Alter", alter, "du darfst Mofa fahren")
if alter >= 16 and alter <= 17:
    print ("Im Alter", alter, "du darfst Moped fahren")
if alter >= 18 and alter <= 88:
    print ("Im Alter", alter, "du darfst Auto fahren")
