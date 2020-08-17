#winning conditions
win = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7]
    ]

#game initialisation
player1 = []
player2 = []

board =[
    " "," "," ",
    " "," "," ",
    " "," "," "
    ]

isP1Turn = True

#winning
def inPlayer(number, player):
    return True if number in player else False

def isWin(player):
    for i in win:
        check = inPlayer(i[0], player) and inPlayer(i[1], player) and inPlayer(i[2], player)
        if check:
            return True
    return False

#method for printing the board
def printRow(in1,in2 ,in3 ):
   print(board[in1] + " | " + board[in2] + " | " + board[in3])

#main game loop
while True:

    #display whose turn is it
    print("Player 1's Turn") if isP1Turn else print("Player 2's Turn")

    #display board
    printRow(6,7,8)
    printRow(3,4,5)
    printRow(0,1,2)

    #take input from player
    playerInp = int(input("Enter board number: "))

    #Checks input
    while True:
        if playerInp not in list(range(1,10)) or board[playerInp-1] != " ":
            playerInp = int(input("Enter board number again: "))
        else:
            break

    #append input to player on current turn
    if isP1Turn:
        player1.append(playerInp)
        board[playerInp-1] = "O"
        isP1Turn = False
    else:
        player2.append(playerInp)
        board[playerInp-1] = "X"
        isP1Turn = True

    
    print("")


    #END GAME CONDITIONS
    #checks if p1 or p2 has won
    if isWin(player1):
        print("PLAYER 1 WINS!!!")
        break
    elif isWin(player2):
        print("PLAYER 2 WINS")
        break

    #checks if board is full
    if len(player1) + len(player2) >= 9:
        print("DRAW")

print(player1, player2)
