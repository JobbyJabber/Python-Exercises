import datetime

def tworzenieRodziny(listaRodziny):
    ile = int(input("Ile członków ma Twoja rodzina? "))
    # rodzina = [[] for czlonek in range(ile)]
    osoba = []
    for x in range(ile):
        imie = input("Podaj imie czlonka: ")
        wiek = int(input("Podaj wiek członka: "))
        gender = input("Podaj płeć: ")
        pesel = stworzPesel(wiek, gender)
        zarobki = input("Podaj zarobki rodziców: ")            
        osoba.extend([imie, wiek, gender, pesel, zarobki])
        listaRodziny.append(osoba)
        osoba = []
    return listaRodziny


def dodawanieCzlonka(rodzina):
    osoba = []
    imie = input("Podaj imie czlonka: ")
    wiek = int(input("Podaj wiek członka: "))
    gender = input("Podaj płeć: ")
    pesel = stworzPesel(wiek, gender)
    zarobki = input("Podaj zarobki rodziców: ")            
    osoba.extend([imie, wiek, gender, pesel, zarobki])
    rodzina.append(osoba)
    if wiek > 40: 
        print("Dzień dobry " + imie)
    else:
        print("Cześć " + imie)
    return rodzina


def usuwanieCzlonka(rodzina):
    delete = int(input("Podaj pesel członka, którego chcesz usunąć? "))
    for i in range(len(rodzina)):
        if int(rodzina[i][3]) == delete:
            del rodzina[i]
            return rodzina
    print("Nie znaleziono członka rodziny z takim peselem")
    return rodzina


def stworzPesel(wiek, gender):
    iscorrect = False
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = int(date.strftime("%Y"))
    year = str(year - wiek)[2:4]
    while not iscorrect:
        try:
            pesel = input("Wprowadź swój pesel: ")
            int(pesel)
            if len(pesel) != 11:
                raise Exception("Pesel powinien mieć 11 znaków")
            if not pesel[0:2] == year:
                raise Exception("Wiek nie jest taki sam jak pesel")
            if int(pesel[-2]) % 2 == 0 and not gender == "F":
                raise Exception("Nieprawidłowa płeć")
            if int(pesel[-2]) % 2 == 0 and gender == "M": 
                raise Exception("Nieprawidłowa płeć")
            iscorrect = True
            return pesel
        except Exception as error:
            print(error)


def menu():
    rodzina = []
    exit = False
    while not exit:
        print("Menu Aplikacji")
        print("1 - Stworzenie rodziny")
        print("2 - Dodaj członka")
        print("3 - Usuń członka")
        print("4 - Wyświetl członka")
        print("X - wyłącz")
        wybor = input("Wprowadź Twój wybór: ").lower()
        if wybor == "x":
            print("Program zostanie wyłączony")
            exit = True
        elif wybor == "1":
            rodzina = tworzenieRodziny(rodzina)
            print(rodzina)
        elif wybor == "2":
            rodzina = dodawanieCzlonka(rodzina)
        elif wybor == "3":
            rodzina = usuwanieCzlonka(rodzina)
        elif wybor == "4":
            print(rodzina)
        else:
            print("Nieprawidłowa komenda!")

menu()
