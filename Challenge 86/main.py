'''
Challenge 86: Tic-tac-toe... with numbers
Let's solve a tic-tac-toe problem :smilecat:

Task
You are given a number n and n testcases follow for each testcase, you are given a starting player x or o and then you are given the moves made between x and o alternatively

So if the moves are 12569 and x starts,
1 - x
2 - o
5 - x
6 - o
9 - x

you have to output the winner(X or O) if there is any otherwise output Tie

The positions on the board are as follows
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

Example
Input:
2
X 5
1 2 5 6 9
X 9
1 3 2 4 6 9 7 5 8

Output:
X
Tie


Challenge suggested by @KK1729#1045

'''


def TicTacToe(gameStarter, _position = None):

    _position = str(_position)

    position = []
    for char in _position:
        if(char == " "):
            continue
        position.append(int(char))

    whoseMove = gameStarter[0]
    winner = None

    gameBoard = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]]

    for move in position:

        Xpos = (move-1) // 3
        Ypos = (move-1) % 3

        gameBoard[Xpos][Ypos] = whoseMove

        if(HasWon(gameBoard)):
            return HasWon(gameBoard)

        if(whoseMove == "X"):
            whoseMove = "O"
        else:
            whoseMove = "X"


    return "Tie"



def HasWon(_gameBoard):
    if(_gameBoard[0][0]):
        # horizontal
        if(CheckWinning(_gameBoard[0][0], _gameBoard[0][1], _gameBoard[0][2])):
            return _gameBoard[0][0]

        # vertical
        if(CheckWinning(_gameBoard[0][0], _gameBoard[1][0], _gameBoard[2][0])):
            return _gameBoard[0][0]

        # slanting
        if(CheckWinning(_gameBoard[0][0], _gameBoard[1][1], _gameBoard[2][2])):
            return _gameBoard[0][0]
        
    if(_gameBoard[0][1]):
        # vertical
        if(CheckWinning(_gameBoard[0][1], _gameBoard[1][1], _gameBoard[2][1])):
            return _gameBoard[0][1]
        
    if(_gameBoard[0][2]):
        # vertical
        if(CheckWinning(_gameBoard[0][2], _gameBoard[1][2], _gameBoard[2][2])):
            return _gameBoard[0][2]

        # slanting
        if(CheckWinning(_gameBoard[0][2], _gameBoard[1][1], _gameBoard[2][0])):
            return _gameBoard[0][2]
            
    if(_gameBoard[1][0]):
        # horizontal
        if(CheckWinning(_gameBoard[1][0], _gameBoard[1][1], _gameBoard[1][2])):
            return _gameBoard[1][0]
    
    if(_gameBoard[2][0]):
        # horizontal
        if(CheckWinning(_gameBoard[2][0], _gameBoard[2][1], _gameBoard[2][2])):
            return _gameBoard[2][0]

        

def CheckWinning(place1, place2, place3):
    if(place1 == place2 and place1 == place3):
        return True
    else:
        return False

no_of_times = input()

for i in range(int(no_of_times)):
    InputWhoStarts = input()
    InputPosition = input()
    print(TicTacToe(InputWhoStarts, InputPosition))

