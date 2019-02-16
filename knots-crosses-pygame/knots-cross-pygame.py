import pygame

'''
A reimplementation of the knots and crosses game - this time using the 
pygame module to create an interactive user interface, allowing players
to use the mouse instead.
'''

pygame.font.init()

white_colour = (255, 255, 255)
clock = pygame.time.Clock()
tick_rate = 60

font = pygame.font.SysFont('comicsacs', 75)

background_image = pygame.image.load('board.png')
background_image = pygame.transform.scale(background_image, (500, 500))
cross_image = pygame.image.load('cross.png')
cross_image = pygame.transform.scale(cross_image, (125, 125))
knot_image = pygame.image.load('knot.png')
knot_image = pygame.transform.scale(knot_image, (125, 125))

# size = 3
def buildBoard(size):
    board = []
    for i in range(0,size):
        row = [" "]*size
        board.append(row)
    return board

class Board: # a game of knots and crosses

    def __init__(self):
        self.board = buildBoard(3)
        self.finishedGame = False

        self.spacesFilled = 0

        self.turn = 0 # 0 or 1

    '''
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
    '''

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

    def draw(self, row, column):
        if self.checkPositionEmpty(row, column):
            if self.turn == 0:
                self.board[row][column] = "O"
                self.turn = 1
            elif self.turn == 1:
                self.board[row][column] = "X"
                self.turn = 0
            self.spacesFilled += 1

class Game:
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 600
        self.screen_title = "Knots and Crosses"

        self.game_screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.game_screen.fill(white_colour)
        pygame.display.set_caption(self.screen_title)

        self.score_O = 0
        self.score_X = 0



    def game_loop(self):
        board = Board()

        tie = False
        did_win = False
        is_game_over = False
        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    if (0 < pos[0] < 164) and (0 < pos[1] < 141):
                        print('top left')
                        board.draw(0, 0)
                    elif (186 < pos[0] < 327) and (9 < pos[1] < 141):
                        print('top middle')
                        board.draw(0, 1)
                    elif (349 < pos[0] < 494) and (3 < pos[1] < 139):
                        print('top right')
                        board.draw(0, 2)

                    elif (1 < pos[0] < 163) and (177 < pos[1] < 317):
                        print('middle left')
                        board.draw(1, 0)
                    elif (185 < pos[0] < 329) and (178 < pos[1] < 318):
                        print('middle middle')
                        board.draw(1, 1)
                    elif (350 < pos[0] < 494) and (179 < pos[1] < 317):
                        print('middle right')
                        board.draw(1, 2)

                    elif (1 < pos[0] < 161) and (353 < pos[1] < 494):
                        print('bottom left')
                        board.draw(2, 0)
                    elif (184 < pos[0] < 329) and (354 < pos[1] < 491):
                        print('bottom middle')
                        board.draw(2, 1)
                    elif (351 < pos[0] < 494) and (355 < pos[1] < 495):
                        print('bottom right')
                        board.draw(2, 2)


                # print(event)

            self.game_screen.fill(white_colour)
            self.game_screen.blit(background_image, (0, 0))
            points_O = font.render(str(self.score_O), True, (0, 0, 0))
            points_X = font.render(str(self.score_X), True, (0, 0, 0))
            self.game_screen.blit(points_O, (20, 520))
            self.game_screen.blit(points_X, (450, 520))


            if board.board[0][0] == "X":
                self.game_screen.blit(cross_image, (25, 10))
            elif board.board[0][0] == "O":
                self.game_screen.blit(knot_image, (25, 10))
            if board.board[0][1] == "X":
                self.game_screen.blit(cross_image, (195, 13))
            elif board.board[0][1] == "O":
                self.game_screen.blit(knot_image, (195, 13))
            if board.board[0][2] == "X":
                self.game_screen.blit(cross_image, (354, 10))
            elif board.board[0][2] == "O":
                self.game_screen.blit(knot_image, (354, 10))

            if board.board[1][0] == "X":
                self.game_screen.blit(cross_image, (25, 184))
            elif board.board[1][0] == "O":
                self.game_screen.blit(knot_image, (25, 184))
            if board.board[1][1] == "X":
                self.game_screen.blit(cross_image, (192, 184))
            elif board.board[1][1] == "O":
                self.game_screen.blit(knot_image, (192, 184))
            if board.board[1][2] == "X":
                self.game_screen.blit(cross_image, (357, 184))
            elif board.board[1][2] == "O":
                self.game_screen.blit(knot_image, (357, 184))


            if board.board[2][0] == "X":
                self.game_screen.blit(cross_image, (25, 359))
            elif board.board[2][0] == "O":
                self.game_screen.blit(knot_image, (25, 359))
            if board.board[2][1] == "X":
                self.game_screen.blit(cross_image, (192, 359))
            elif board.board[2][1] == "O":
                self.game_screen.blit(knot_image, (192, 359))
            if board.board[2][2] == "X":
                self.game_screen.blit(cross_image, (357, 359))
            elif board.board[2][2] == "O":
                self.game_screen.blit(knot_image, (357, 359))

            if board.checkWin("X"):
                did_win = True
                self.score_X += 1
                text = font.render("X wins", True, (0, 0, 0))
                self.game_screen.blit(text, (160, 510))
                pygame.display.update()
                clock.tick(1)
                break
            elif board.checkWin("O"):
                did_win = True
                self.score_O += 1
                text = font.render("O wins", True, (0, 0, 0))
                self.game_screen.blit(text, (160, 510))
                pygame.display.update()
                clock.tick(1)
                break

            if board.checkBoardFull():
                tie = True
                text = font.render("Draw", True, (0, 0, 0))
                self.game_screen.blit(text, (190, 510))
                pygame.display.update()
                clock.tick(1)
                break

            pygame.display.update()
            clock.tick(tick_rate)

        if did_win or tie:
            self.game_loop()


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.game_loop()
    pygame.quit()
    quit()