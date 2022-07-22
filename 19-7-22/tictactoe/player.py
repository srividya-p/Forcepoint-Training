from board import Board

class Player:
    def __init__(self, userName, symbol) -> None:
        self.userName = userName
        self.symbol = symbol

    def placeMove(self, cell):
        if cell.isMarked():
            print("Position occupied.")
            return False
        cell.symbol = self.symbol
        print("Cell marked.")
        return True