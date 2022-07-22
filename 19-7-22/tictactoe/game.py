from player import Player
from board import Board

game = None

class Game:
    def __init__(self, playerX, playerO) -> None:
        self.playerX = playerX
        self.playerO = playerO
        self.board = Board.createBoard()
        self.currentSymbol = 'x'

    @staticmethod
    def createGame(playerX = Player('player1', 'x'), playerO = Player('player2', 'o')):
        global game
        if game != None: 
            print('Game is a singleton.')
            return game
        game = Game(playerX, playerO)
        return game

    #UPDATE
    # def play(self):
    #     while True:
    #         pass

    def startGame(self):
        isGameEnd, winner = False, None
        self.board.printBoard()
        while(not isGameEnd):
            if self.currentSymbol == 'x':
                print("Player X Moves = ", end = " ")
                i, j = map(int, input().split(' '))
                if i<0 or i>2 or j<0 or j>2: 
                    print('Incorrect index.')
                    continue
                isPlaced, message = self.playerX.placeMove(self.board.cells[i][j])
                print(message)
                if not isPlaced: continue
                self.board.printBoard()
            elif self.currentSymbol == 'o':
                print("Player O Moves = ", end = " ")
                i, j = map(int, input().split(' '))
                if i<0 or i>2 or j<0 or j>2: 
                    print('Incorrect index.')
                    continue
                isPlaced, message = self.playerO.placeMove(self.board.cells[i][j])
                print(message)
                if not isPlaced: continue
                self.board.printBoard()
            self.currentSymbol = 'o' if self.currentSymbol == 'x' else 'x'
            isGameEnd, winner = self.board.isWinningStateReached()

        print(f"Winner is {self.playerX.userName if winner == 'x' else self.playerO.userName} {winner}")

g = Game.createGame()
# g.startGame()

g1 = Game.createGame()
