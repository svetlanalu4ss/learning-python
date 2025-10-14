
alpha = int (input ("Gib alpha ein:\n"))
beta = int (input ("Gib beta ein:\n"))
gamma = int (input ("Gib gamma ein:\n"))
summe = alpha + beta + gamma

if alpha < 0 or beta < 0 or gamma <0:
    print ("Kein gultiges Dreieck: Die Winkel mussen positiv sein")
elif summe <= 179:
    print ("Kein gultiges Dreieck: Die Winkelsumme ist nicht 180 Grad")
elif alpha > beta and alpha > gamma and alpha != beta and alpha != gamma and summe == 180:
    print ("Das ist ein stumpfwinkliges Dreieck")
elif alpha == 90 or beta == 90 or gamma == 90 and summe == 180:
    print ("Das ist ein rechtwinkliges Dreieck")
elif alpha == beta == gamma and summe == 180:
    print ("Das ist ein spitzwinkliges Dreieck")
elif beta == gamma or gamma == alpha and summe == 180:
    print ("Das ist ein spitzwinkliges Dreieck")

alpha = 90
beta = 45
gamma = 45
summe = alpha + beta + gamma
if summe == 180:
    if alpha > 0 and beta > 0 and gamma > 0:
        if alpha == 90 or beta == 90 or gamma == 90:
            print ("Das ist ein reechwinkliges Dreieeck")
        elif alpha > 90 or beta or gamma > 90:
            print ("")
        else:
            print ("Das ist spitzwin")
            
