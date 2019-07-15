#winning condition
win = [[1,2,3],
        [4,5,6],
        [7,8,9],
        [1,4,7],
        [2,5,8],
        [3,6,9],
        [1,5,9],
        [3,5,7]]

#game initialisation
player1 = []
player2 = []

board =[" "," "," "," "," "," "," "," "," "]

isRunning = True
isP1Turn = True

#winning
def isWin(player,counter):
    global win
    x = False
    while not x:
        for i in win:
            if i[0] and i[1] and i[2]  in player:
                x = True
                return True

#method for printing the board
def printRow(in1,in2 ,in3 ):
   print(board[in1] + " | " + board[in2] + " | " + board[in3])

#main game loop
while isRunning:
    playerInp = int(input("Enter board number: "))
    while True:
        if playerInp not in [1,2,3,4,5,6,7,8,9] or board[playerInp-1] is not " ":
            playerInp = int(input("Enter board number again: "))
        else:
            break

    if isP1Turn is True:
        player1.append(playerInp)
        board[playerInp-1] = "O"
        isP1Turn = False
    else:
        player2.append(playerInp)
        board[playerInp-1] = "X"
        isP1Turn = True

    printRow(0,1,2)
    printRow(3,4,5)
    printRow(6,7,8)
    
    if isWin(player1,0):
        print("player 1 has won")
        isRunning = False
    elif isWin(player2,0):
        print("player 2 has won")
        isRunning = False

    if len(player1) + len(player2) is 9:
        isRunning = False

print(player1, player2)
