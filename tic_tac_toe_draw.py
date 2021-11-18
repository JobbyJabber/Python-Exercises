board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def displayBoard():
    for i in range(0, 3):
        print(f"{board[i][0]}", "|", f"{board[i][1]}", "|", f"{board[i][2]}")
def userInput():
    row1 = input("Enter your row: ")
    col1 = input("enterur")
def getValues(move):
    return 1, 2


# isValid('1,3')
displayBoard()
# startGame()




# def startGame():
#     moves = 0
#     isX = True
#     game_finished = False
#     while not game_finished:
#         if moves == 9:
#             #potem odbugować żeby było tyle ruchów ile trzeba
#             break
#         user_move = input('Enter your coordiantes separated by comma (1,3): ')
#         if(isValid(user_move)):
#             value = 'X'
#             if not isX:
#                 value = 'Y'
#             i, j = getValues(user_move)
#             board[i][j] = value
#             moves += 1
#             isX = False


# def isValid(move):
#     splited = move.split(',')
#     # ['1', '5']

#     if board[int(splited[0])][int(splited[1])] == 'X' or board[int(splited[0])][int(splited[1])] == 'Y':
#         # //False
#         print(splited)
