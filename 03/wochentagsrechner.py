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

    
# Просим пользователя ввести день недели как число от 0 до 6
# 0 = Montag, 1 = Dienstag, ..., 6 = Sonntag
wochentag_nummer = int(input("Gib eine Zahl für den Wochentag ein (0=Montag, 6=Sonntag): "))

# Присваиваем имя дня недели через простую цепочку if
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

# Выводим день недели
print("Wochentag:", wochentag_name)

# Проверяем, выходной это или рабочий день
if wochentag_nummer >= 5:
    print("Das ist ein Wochenende.")  # суббота или воскресенье
else:
    print("Das ist ein Arbeitstag.")  # понедельник-пятница