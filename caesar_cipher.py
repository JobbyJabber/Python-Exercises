import string


def wprowadzWyraz():
    # Funkcja sprwadza zapisuje wyraz albo czy wyraz jest tajnym kodem
    wyraz = input("Wprowadź swój wyraz: ")
    if 'urce' in wyraz or 'URCE' in wyraz:
        print("WYKRYTO TAJNY KOD")
        print("Hasło do WIFI: CycekDebil123")
    return wyraz




def szyfrowanie(litera, alfabet):
    # Funkcja szyfruje podany wcześniej wyraz
    if litera == " ":
        return " "
    numer_w_alfabecie = alfabet.index(litera)
    # sprawdza numer w alfabecie
    po_dodaniu = numer_w_alfabecie + ile
    # bierze numer literki po dodaniu naszej cyfry
    if po_dodaniu > 25:
        po_dodaniu = po_dodaniu-26
    zaszyfrowany_znak = alfabet[po_dodaniu]
    # znak który będzie po zmianie
    return zaszyfrowany_znak


wyraz = wprowadzWyraz()
zaszyfrowany_wyraz = ""
ile = int(input("O ile miejsc przestawiać: "))
while ile % 26 == 0:
    # pętla nie pozwala wprowadzić wielkrotności 26, ponieważ wtedy szyfr będzie wyglądał tak samo
    ile = int(input("Wprowadź inną liczbę"))
alfabet_malych = string.ascii_lowercase
alfabet_duzych = string.ascii_uppercase
for i in wyraz:
    # pętla która sprawdza wielkość znaków, a potem wykonuje funkcje szyforwanie. 
    if i in alfabet_malych:
        zaszyfrowany_znak = szyfrowanie(i, alfabet_malych)
        zaszyfrowany_wyraz += zaszyfrowany_znak
    else:
        zaszyfrowany_znak = szyfrowanie(i, alfabet_duzych)
        zaszyfrowany_wyraz += zaszyfrowany_znak
print(zaszyfrowany_wyraz)



# a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y z
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
