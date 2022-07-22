from symtable import Symbol


from board import Board

class Player:
    def __init__(self, userName, symbol) -> None:
        self.userName = userName
        self.symbol = symbol

    def placeMove(self, cell):
        if cell.isMarked():
            return False, "Position occupied."
        cell.symbol = self.symbol
        return True, "Cell marked."