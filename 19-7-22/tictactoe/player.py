from symtable import Symbol


from board import Board

class Player:
    def __init__(self, userName, symbol) -> None:
        self.userName = userName
        self.symbol = symbol

    def placeMove(self, i, j, board):
        return board.setCell(i, j, self.symbol)