
#Schreibe ein Programm, das den Benutzer nach der aktuellen Uhrzeit 
# in einer bestimmten Zeitzone fragt (z. B. "Berlin", "New York", "Tokyo") 
# und eine Ausgabe der aktuellen Zeit in einer anderen Zeitzone liefert. 
# Du kannst das Programm so gestalten, dass es die Zeitdifferenzen für die Zeitzonen ausgibt.
#Beispiel:
 
#Gib die Zeitzone ein (Berlin, New York, Tokyo): Berlin
#Gib die aktuelle Uhrzeit ein (im 24-Stunden-Format, z.B. 14:30): 14:30
#Die Uhrzeit in New York ist 08:30.
#Hinweis: Du kannst für die Zeitumrechnung mit festen Stundenunterschieden arbeiten 

# (z. B. Berlin ist UTC+1, New York ist UTC-5 Токио → UTC+9). 
# Bei einer erweiterten Version könntest du auch mit der datetime-Bibliothek arbeiten, 
# aber für den Einstieg reicht eine einfache Berechnung mit festen Zeitverschiebungen.

# разница = UTC(город_цель) − UTC(город_выбор)
# время_цель = время_выбор + разница

zone = input("Gib die Zeitzone ein (Berlin, New York, Tokyo):\n")
stunden = int (input("Gib die aktuelle Stunden ein (0-24):\n"))
minuten = int (input("Gib die aktuelle Minuten ein (00-59):\n"))

if zone == "Berlin":
    berlin = stunden
    new_york = stunden - 6 # −5 − (+1) = −6
    tokyo = stunden + 8 # +9 − (+1) = +8
    print("In Berlin jetzt:", berlin, ":", minuten, "Uhr")

elif zone == "New York":
    new_york = stunden
    berlin = stunden + 6 # +1-(-5) = 6
    tokyo = stunden +14 # +9 - (-5) = 14
    print("In New York jetzt:", new_york, ":", minuten, "Uhr")

elif zone == "Tokyo":
    tokyo = stunden
    berlin = stunden - 8 # +1 - (+9) = - 8 
    new_york = stunden -14 # -5 -(+9) = -14
    print("In Tokyo jetzt:", tokyo, ":", minuten, "Uhr")

else:
    print("Unbekannte Zeitzone")



zone = input("Gib die Zeitzone ein (Berlin, New York, Tokyo):\n")
stunden = int(input("Gib die aktuelle Stunde ein (0–23):\n"))
minuten = int(input("Gib die aktuelle Minute ein (00–59):\n"))

if zone == "Berlin":
    berlin = stunden
    new_york = (stunden - 6) % 24  # −5 − (+1) = −6
    tokyo = (stunden + 8) % 24     # +9 − (+1) = +8
    print("In Berlin:", berlin, ":", minuten)
    print("In New York:", new_york, ":", minuten)
    print("In Tokyo:", tokyo, ":", minuten)

elif zone == "New York":
    new_york = stunden
    berlin = (stunden + 6) % 24
    tokyo = (stunden + 14) % 24
    print("In New York:", new_york, ":", minuten)
    print("In Berlin:", berlin, ":", minuten)
    print("In Tokyo:", tokyo, ":", minuten)

elif zone == "Tokyo":
    tokyo = stunden
    berlin = (stunden - 8) % 24
    new_york = (stunden - 14) % 24
    print("In Tokyo:", tokyo, ":", minuten)
    print("In Berlin:", berlin, ":", minuten)
    print("In New York:", new_york, ":", minuten)

else:
    print("Unbekannte Zeitzone.")

  
  
  # if stunden >= 24:
   #   stunden = stunden - 24
