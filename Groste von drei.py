#  Findet die größte von drei eingegebenen Zahlen.

zahl1 = float (input ("Die erste Zahl ist:\n"))
zahl2 = float (input ("Die Zweite Zahl ist:\n"))
zahl3 = float (input ("Die Dritte Zahl ist:\n"))
if zahl1 > zahl2 and zahl1 > zahl3:
    print ("Die größte Zahl ist:",zahl1)
elif zahl2 > zahl1 and zahl2 > zahl3:
    print ("Die größte Zahl ist:",zahl2)
elif zahl3 > zahl1 and zahl3 > zahl2:
    print ("Die größte Zahl ist:",zahl3)
else:
    print("Die Zahlen sind gleich oder es gibt mehrere gleiche größte Zahlen.")




