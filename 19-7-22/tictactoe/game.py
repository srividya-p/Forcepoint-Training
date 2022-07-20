from player import Player
from board import Board

class Game:
    def __init__(self, playerX = Player('player1', 'x'), playerO = Player('player2', 'o')) -> None:
        self.playerX = playerX
        self.playerO = playerO
        self.board = Board.createBoard()
        self.currentSymbol = 'x'

    def startGame(self):
        isGameEnd, winner = False, None
        while(not isGameEnd):
            if self.currentSymbol == 'x':
                print("Player X Moves = ", end = " ")
                i, j = map(int, input().split(' '))
                isPlaced, message = self.playerX.placeMove(i, j, self.board)
                print(message)
                if not isPlaced: continue
            elif self.currentSymbol == 'o':
                print("Player O Moves = ", end = " ")
                i, j = map(int, input().split(' '))
                isPlaced, message  = self.playerO.placeMove(i, j, self.board)
                print(message)
                if not isPlaced: continue
            self.currentSymbol = 'o' if self.currentSymbol == 'x' else 'x'
            isGameEnd, winner = self.board.isWinningStateReached()

        print(f"Winner is {self.playerX.userName if winner == 'x' else self.playerO.userName} {winner}")

g = Game()
g.startGame()