ile = int(input("Ile członków ma Twoja rodzina?"))
rodzina = [[] for czlonek in range(ile)]
i=0
while ile > i:
    imie = input("Podaj imie czlonka: ")
    wiek = int(input("Podaj wiek członka: "))
    gender = input("Podaj płeć: ")
    pesel = input("Podaj pesel: ")
    zarobki = input("Podaj zarobki rodziców: ")
    for x in range(ile):              
        rodzina[x].append(imie)
        rodzina[x].append(wiek)
    i += 1
def Rodziny():

def tworzenieCzlonka():
    imie = input("Podaj imie czlonka: ")
    wiek = int(input("Podaj wiek członka: "))
    gender = input("Podaj płeć: ")
    pesel = input("Podaj pesel: ")
    zarobki = input("Podaj zarobki rodziców: ")
