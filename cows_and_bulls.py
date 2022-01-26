###### NOT ENDED YET(bagels is almnost the same) #######

import random
numbers = []
lista = '1 2 3 4 5 6 7 8 9'.split()


def generateNumber():

    for i in range(1, 5):
        i = random.choice('1 2 3 4 5 6 7 8 9'.split())
        numbers.append(i)
    return numbers


def checkGuess(nums):
    cow = 0
    bull = 0
    x = 0
    while x < 10:
        xinput = input('Enter a number: ')
        if xinput in nums:
            cow = cow + 1
        else:
            bull = bull + 1
        x = x + 1
    print("bull " * bull, "cow " * cow)
    return cow, bull


generateNumber()

checkGuess(numbers)
