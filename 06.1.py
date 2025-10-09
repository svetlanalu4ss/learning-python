# Aufgabe: Altersprufung fur Mofa, Moped und Auto
# Mofa: ab 14
# Moped: ab 16
#Auto: ab 18
# Eingabe, die ganzzahlige weertee annimt und dann ausgibt von 0 bis 89,
#welche Fahrzeug (Mofa,Moped oder Auto) empfolen wird
#wenn die Eingabe nicht ganzzahlig ist,oder unter null, soll eine entsprechende Fehlermeldung ausgegeben weerden

alter = input ("Wie alt bist du?")
if (alter.isnumeric () and int (alter) <=89):
    print ("Alteer ist ganzzahlig")
else:
    print ("Eingabe inkorrekt")






print("test")
alter = input("Wie alt bist du?\n")
print("ich bin", alter, "Jahre alt")

#Body maß ind
#Berehnung mit festeen Variablen
große = 1.8
gewicht = 500
bmi = ( gewicht / große ** 2 ) #große hoch2 = Große im Quadrat
print ("Ihr BMI ist: ", bmi )
#Berechnung mit Input
grosse = float (input ("Geben Sie Ihre Größe an: "))
gewicht = float (input ('Geben Sie Ihre Körpergröße an: '))
BMI = gewicht / (grosse ** 2)
print ("Ihr BMI ist: ", BMI )
#Berechnung der Fläche  eines Kreises bei Eingabe des Radius 
radius = float (input ("Geben Sie den Radius an:  "))
fläche = 3.143 * (radius ** 2)
print ("Die Fläche beträgt: ", fläche)