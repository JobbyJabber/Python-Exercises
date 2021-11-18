####### BAGELS #######
import random
import time

lista = '1 2 3 4 5 6 7 8 9'.split()
#List where we have our range of random.
randomChoice = []
def startUp():
    print("I am thinking of a 3-digit number. Try to guess what it is.")
    time.sleep(1)
    print('''Here are some clues:
                When I say:    That means:
                Pico         One digit is correct but in the wrong position.
                Fermi        One digit is correct and in the right position.
                Bagels       No digit is correct.''')
    time.sleep(3)
    print("I have thought up a number.")
    time.sleep(1)
    print("You Have 10 guesses to get it. ")

def generateNumber():
    #Function to generate number which gonna be guessed
    for i in range(0,3):
        number = random.choice(lista)
        randomChoice.append(number)
    return randomChoice


def userGuess():
    #Checking user input if its FERMI/PICO/BAGELS
    x=0
    
    while x < 11:
        guess = list(input("Enter your guess: "))
        if guess == ['s', 't', 'o', 'p']:
            break 
        if guess == ["2", "1", "3", "7"]:
            # EasterEgg
            c = True
            while c == True:
                print("Psy jadą ci wpierdolić io io!!!")
        while len(guess) != 3:
            guess = list(input("Enter 3 digits number!: "))
        print("Guess #",x+1)
        if guess == randomChoice:
            print("You Got it!")
            randomChoice.clear()
            break
        for i in range (0,3):
            if guess[i] == randomChoice[i]:
                print('FERMI')   
            elif guess[i] in randomChoice:
                print("PICO")
            else: 
                print("BAGELS")
        x += 1
        if x == 10:
            print("Numbers was: ", randomChoice) 
        guess.clear()
    
        


czy = "Y"
while czy == "Y":
    startUp()
    generateNumber()
    userGuess()
    czy = input("Do you want to play again? (Y/N)")