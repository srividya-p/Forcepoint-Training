from player import Player
from board import Board

game = None

class Game:
    def __init__(self, playerX, playerO) -> None:
        self.playerX = playerX
        self.playerO = playerO
        self.board = Board.createBoard()
        self.currentSymbol = 'x'
        self.i, self.j = 0, 0

    @staticmethod
    def createGame(playerX = Player('player1', 'x'), playerO = Player('player2', 'o')):
        global game
        if game != None: 
            print('Game is a singleton.')
            return game
        game = Game(playerX, playerO)
        return game

    def acceptInputAndValidate(self, turn):
        print(f"Player {turn} Moves = ", end = " ")
        self.i, self.j = map(int, input().split(' '))
        if self.i<0 or self.i>2 or self.j<0 or self.j>2: 
            print('Incorrect index.')
            return False
        return True

    def startGame(self):
        isGameEnd, winner = False, None
        self.board.printBoard()
        
        while(not isGameEnd):
            if self.currentSymbol == 'x':
                isInputSet = self.acceptInputAndValidate('X')
                if not isInputSet: continue
                isPlaced = self.playerX.placeMove(self.board.cells[self.i][self.j])
                if not isPlaced: continue
                self.board.printBoard()
            elif self.currentSymbol == 'o':
                isInputSet = self.acceptInputAndValidate('O')
                if not isInputSet: continue
                isPlaced = self.playerO.placeMove(self.board.cells[self.i][self.j])
                if not isPlaced: continue
                self.board.printBoard()
            
            self.currentSymbol = 'o' if self.currentSymbol == 'x' else 'x'
            isGameEnd, winner = self.board.isWinningStateReached()

        print(f"Winner is {self.playerX.userName if winner == 'x' else self.playerO.userName} {winner}")

g = Game.createGame()
g.startGame()
