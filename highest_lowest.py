
def high_and_low(numbers):

    numbers = numbers.split(' ')
    nums = list
    for i in range (0, len(numbers)):
        numbers[i] = int(numbers[i])
    max1 = max(numbers)
    min1 = min(numbers)
    napis = f"{max1} {min1}"
    print(napis)
    return napis

high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")