import copy

class Board :
    def __init__( self, c1, c2 ) :
        self.state = [['-','-','-'],
                      ['-','-','-'],
                      ['-','-','-']]
        self.winner = None
        self.nextMove = 0
        self.history = []
        self.char = [c1,c2]
        self.default = '-'

    def checkForWinner(self) :
        rowWin = False
        colWin = False
        diaWin = False

        for i in range(0,3):
            if (self.state[i][0] == self.state[i][1] and self.state[i][1] == self.state[i][2]):
                if ( self.default == self.state[i][0] ):
                    continue
                rowWin = True
                if ( self.state[i][0] == self.char[0] ):
                    self.winner = 1
                else :
                    self.winner = 2

        for i in range(0,3):
            if (self.state[0][i] == self.state[1][i] and self.state[1][i] == self.state[2][i]):
                if ( self.default == self.state[0][i] ):
                    continue
                colWin = True
                if ( self.state[0][i] == self.char[0] ):
                    self.winner = 1
                else :
                    self.winner = 2

        if ( self.state[0][0] == self.state[1][1] and self.state[1][1] == self.state[2][2]):
            diaWin = True
            if ( self.default == self.state[1][1] ):
                pass
            elif ( self.state[1][1] == self.char[0] ):
                self.winner = 1
            else :
                self.winner = 2
        elif ( self.state[2][0] == self.state[1][1] and self.state[1][1] == self.state[0][2]):
            diaWin = True
            if ( self.default == self.state[1][1] ):
               pass 
            elif ( self.state[1][1] == self.char[0] ):
                self.winner = 1
            else :
                self.winner = 2

    def checkForDraw(self) :
        left = False

        for i in range(0,3):
            for j in range(0,3):
                if self.state[i][j] == self.default :
                    left = True
                    break

        return left

    def move (self, player, cellNumber):
        cellNumber -= 1

        if self.state[cellNumber//3][cellNumber%3] == self.default :
            self.state[cellNumber//3][cellNumber%3] = self.char[player-1]
            self.nextMove = 1 - self.nextMove

        currentState = copy.deepcopy(self.state)

        self.history.append(currentState)

        self.checkForWinner();

        if( self.winner != None ):
            print("Game Ends, Player ", self.winner, " wins.")
            print("*"*20)
            print("History : ")
            for i in range (len(self.history)) :
                print("After Move ", i+1, " :",)
                for j in range (len(self.history[i])):
                    print( self.history[i][j] )
            print("*"*20)
            return 0
        elif ( not self.checkForDraw() ):
            print("Nobody deserves to win")
            print("*"*20)
            print("History : ")
            for i in range (len(self.history)) :
                print("After Move ", i+1, " :")
                for j in range (len(self.history[i])):
                    print( self.history[i][j] )
            print("*"*20)
            return 0
        else :
            return 1

game = Board('X', 'O')

gameOn = 1

while ( gameOn ):
        prompt = "Player " + str(game.nextMove + 1) + " to play. \n"
        x = int(input(prompt))
        gameOn = game.move(game.nextMove, x)
        # print( game.history )

