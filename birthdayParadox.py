import datetime, random


def getBirtday(numberOfBirthDays): #my tu będziemy wpisywać potem ile generować
    birthdays = []
    for i in range(numberOfBirthDays):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday.strftime("%b"))
    print(birthdays)
    return birthdays


getBirtday(int(input("Ile ich ma być? ")))

#Not finished yet.
