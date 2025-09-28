from datetime import datetime

datum_text = input("Gib ein Datum im Format TT.MM.JJJJ ein: ")

datum = datetime.strptime(datum_text, "%d.%m.%Y")
wochentag_nummer = datum.weekday()

if wochentag_nummer == 0:
    wochentag_name = "Montag"
if wochentag_nummer == 1:
    wochentag_name = "Dienstag"
if wochentag_nummer == 2:
    wochentag_name = "Mittwoch"
if wochentag_nummer == 3:
    wochentag_name = "Donnerstag"
if wochentag_nummer == 4:
    wochentag_name = "Freitag"
if wochentag_nummer == 5:
    wochentag_name = "Samstag"
if wochentag_nummer == 6:
    wochentag_name = "Sonntag"

print("Wochentag: {wochentag_name}")

if wochentag_nummer >= 5:
    print("Das ist ein Wochenende.")
else:
    print("Das ist ein Arbeitstag.")
