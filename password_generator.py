import random
import string


def generateUpperCaseLetter():
    return random.choice(string.ascii_uppercase)


def generateLowerCaseLetter():
    return random.choice(string.ascii_lowercase)


def generateNumber():
    return str(random.randint(1, 9))


def generate_symbol():
    return random.choice('~ # $ % ^ & * ( )  + = - [ ] / \' . , < > ?'.split())


def generatePassword(liczbaZnakow):
    password = ''
    for _ in range(0, liczbaZnakow):
        choice = random.randint(1, 4)
        if choice == 1:
            password += generateUpperCaseLetter()
        elif choice == 2:
            password += generateLowerCaseLetter()
        elif choice == 3:
            password += generateNumber()
        else:
            password += generate_symbol()
    return password


iloscZnakow = int(input("Ile znaków ma mieć hasło: "))
genteratedPassword = generatePassword(iloscZnakow)
print("Twoje hasło to: ", genteratedPassword)