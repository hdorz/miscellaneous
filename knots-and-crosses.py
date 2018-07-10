import random

'''
A simple knots and crosses game - an introductory exercise in Python 
about object-orientated programming, logic and handling exceptions.
'''

# size = 3
def buildBoard(size):
    board = []
    for i in range(0,size):
        row = [" "]*size
        board.append(row)
    return board

def headsOrTails():
    chance = random.random()
    if chance < 0.5:
        print("Coin flipped for heads.")
        return "H"
    else:
        print("Coin flipped for tails.")
        return "T"

class Board: # a game of knots and crosses

    def __init__(self, nameOne, nameTwo):
        assert nameOne != nameTwo, "Error: Both player names are identical."
        self.board = buildBoard(3)
        self.finishedGame = False

        self.spacesFilled = 0

        self.playerOneName = nameOne
        self.playerTwoName = nameTwo

    def __str__(self):
        prettyRepresentation = "\t\t" + "=====================\n" \
                               "\t\t" + "||" + "  " + self.board[0][0] + "  |  " + self.board[0][1] + "  |  " + self.board[0][2] + "  ||" + "\n" \
                               "\t\t" + "||" + "_____|_____|_____" + "||" + "\n" \
                               "\t\t" + "||" + "  " + self.board[1][0] + "  |  " + self.board[1][1] + "  |  " + self.board[1][2] + "  ||" + "\n" \
                               "\t\t" + "||" + "_____|_____|_____" + "||" + "\n" \
                               "\t\t" + "||" + "  " + self.board[2][0] + "  |  " + self.board[2][1] + "  |  " + self.board[2][2] + "  ||" + "\n" \
                               "\t\t" + "||" + "     |     |     " + "||" + "\n" \
                               "\t\t" + "====================="

        return prettyRepresentation

    def checkPositionEmpty(self, row, column):
        if self.board[row][column] == " ":
            return True

    def checkBoardFull(self): # assists in determining draw
        return (self.spacesFilled == (len(self.board)*len(self.board)))

    # "x and y coordinates"
    def checkWin(self, input):
        checkThis = input
        win = False
        winCount = 0

        moveRight = 0
        for k in range(0, len(self.board)): # run three times
            winCount = 0
            for i in range(0, len(self.board)):
                if (self.board[i][moveRight] == checkThis):
                    winCount += 1
            if winCount == 3:
                win = True
                self.finishedGame = True
                return win
            else:
                moveRight += 1

        moveDown = 0
        for j in range(0, len(self.board)):
            winCount = 0
            for i in range(0, len(self.board)):
                if (self.board[moveDown][i] == checkThis):
                    winCount += 1
            if winCount == 3:
                win = True
                self.finishedGame = True
                return win
            else:
                moveDown += 1

        if self.board[0][0] == checkThis:
            if self.board[1][1] == checkThis:
                if self.board[2][2] == checkThis:
                    win = True
                    self.finishedGame = True
                    return win

        if self.board[0][2] == checkThis:
            if self.board[1][1] == checkThis:
                if self.board[2][0] == checkThis:
                    win = True
                    self.finishedGame = True
                    return win

        return win # if reached here, "win" is False

    def turnKnot(self,row, column):
        self.board[row][column] = "O"
        self.spacesFilled += 1

    def turnCross(self, row, column):
        self.board[row][column] = "X"
        self.spacesFilled += 1

def oneRoundOfKnotsCrosses(name1, name2):
    theBoard = Board(name1, name2)

    passDecisionWhoFlip = False # decide who will flip coin
    while not passDecisionWhoFlip:
        whichPlayer = str(input("Who will flip the coin? (Input player name): "))
        if whichPlayer == theBoard.playerOneName:
            passDecisionPlayerOneFlip = False
            while not passDecisionPlayerOneFlip:
                headTails = str(input(theBoard.playerOneName + ", do you choose heads or tails? (H or T): ")).upper() # user input
                if (headTails.upper() == "H") or (headTails.upper() == "T"):
                    outcome = headsOrTails() # program determining heads or tails
                    if headTails == outcome: # comparing the guesses
                        print(theBoard.playerOneName + " chooses who gets to go first.") # true
                    else:
                        print(theBoard.playerTwoName + " chooses who gets to go first.") # false
                    passDecisionWhoFlip = True
                    passDecisionPlayerOneFlip = True
                else:
                    print("That is not a valid answer. Try again.")
        elif whichPlayer == theBoard.playerTwoName:
            passDecisionPlayerTwoFlip = False
            while not passDecisionPlayerTwoFlip:
                headTails = str(input(theBoard.playerTwoName + ", do you choose heads or tails? (H or T): ")).upper()  # user input
                if (headTails.upper() == "H") or (headTails.upper() == "T"):
                    outcome = headsOrTails()  # program determines heads or tails
                    if headTails == outcome:  # comparing the guesses
                        print(theBoard.playerTwoName + " chooses who gets to go first.")  # true
                    else:
                        print(theBoard.playerOneName + " chooses who gets to go first.")  # false
                    passDecisionWhoFlip = True
                    passDecisionPlayerTwoFlip = True
                else:
                    print("That is not a valid answer. Try again.")
        else:
            print("That is not a valid name. Try again.")

    playerTurn = 0
    passDecisionWhoFirst = False # determines who will go first in the game
    while not passDecisionWhoFirst:
        who = str(input("Who will go first? (Input player name): "))
        if who == theBoard.playerOneName:
            print(theBoard.playerOneName + " will start the game.")
            playerTurn = 1
            passDecisionWhoFirst = True
        elif who == theBoard.playerTwoName:
            print(theBoard.playerTwoName + " will start the game.")
            playerTurn = 2
            passDecisionWhoFirst = True
        else:
            print("That is not a valid name. Try again.")

    end = False
    while not end:
        print(theBoard)
        if playerTurn == 1:
            print("It is " + theBoard.playerOneName + "'s turn.")
            try:
                coordinateRow = int(input("Which row? "))
                coordinateColumn = int(input("Which column? "))
                if theBoard.checkPositionEmpty(coordinateRow, coordinateColumn):
                    theBoard.turnCross(coordinateRow, coordinateColumn)
                    playerTurn = 2
                    if theBoard.checkWin("X") == True:
                        print(theBoard.playerOneName + " has won the game!")
                        end = True
                    elif theBoard.checkBoardFull():
                        print("The game ended up as a draw.")
                        end = True
                else:
                    print("That is not a legal move. Position already filled. Try again.")
            except IndexError:
                print("Please try again. Given coordinates are out of bounds.")
            except ValueError:
                print("Please try again. Given coordinates are invalid.")
        elif playerTurn == 2:
            print("It is " + theBoard.playerTwoName + "'s turn.")
            try:
                coordinateRow = int(input("Which row? "))
                coordinateColumn = int(input("Which column? "))
                if theBoard.checkPositionEmpty(coordinateRow, coordinateColumn):
                    theBoard.turnKnot(coordinateRow, coordinateColumn)
                    playerTurn = 1
                    if theBoard.checkWin("O") == True:
                        print(theBoard.playerTwoName + " has won the game!")
                        end = True
                    elif theBoard.checkBoardFull():
                        print("The game ended up as a draw.")
                        end = True
                else:
                    print("That is not a legal move. Position already filled. Try again.")
            except IndexError:
                print("Please try again. Given coordinates are out of bounds.")
            except ValueError:
                print("Please try again. Given coordinates are invalid.")

    print("===========================================")
    print(theBoard)
    print("===========================================")
    print("Game has finished.")

def game():
    namesAreDifferent = False
    while not namesAreDifferent:
        prompt1 = str(input("Enter name for player 1: "))  # take player names
        prompt2 = str(input("Enter name for player 2: "))
        if prompt1 != prompt2:
            namesAreDifferent = True
        else:
            print("Try again. Names must be different.")
    stop = False
    while not stop:
        oneRoundOfKnotsCrosses(prompt1, prompt2)
        playAgainQuery = False
        while not playAgainQuery:
            askToPlayAgain = str(input("Would you like to play again? (Y or N): ")).upper()
            if (askToPlayAgain.upper() == "Y"):
                print("Restarting game board...\n")
                playAgainQuery = True # stop only inner loop, keep outer loop running
            elif (askToPlayAgain.upper() == "N"):
                print("\n\nEnding program.")
                stop = True # stop outer loop
                playAgainQuery = True # AND inner loop to fully end program
            else:
                print("That is not a valid answer. Try again.") # make the user input again if answer unrecognisable

if __name__ == "__main__":
    game()
