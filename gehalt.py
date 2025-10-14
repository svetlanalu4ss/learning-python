
jahr = int(input("Gib dein Beschaftigungsjahr ein: "))

if jahr == 1:
    salary = 4000
    print ("dein Entgelt ist", salary)

elif jahr == 2 or jahr == 3:
    salary = 4000 + 100 * (jahr - 1)
    print ("dein Entgelt ist", salary)

elif jahr > 3:
    salary = 4300 + 100 * (jahr - 2)
    print ("dein Entgelt ist", salary)

#else :
#      salary = 0  # можно заменить на любое значение или сообщение об ошибке
# print ("Gehalt:", salary)
