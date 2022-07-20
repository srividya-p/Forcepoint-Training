from tkinter import N
from cell import Cell

class Board:
    def __init__(self, cells, winningIndexes) -> None:
        self.cells = cells
        self.winningIndexes = winningIndexes
    
    @staticmethod
    def createBoard():
        rows = []
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append(Cell('_'))
            rows.append(row)
        
        winningIndexes = Board.getWinningIndexes()
        newBoard = Board(rows, winningIndexes)
        return newBoard

    def printBoard(self):
        for row in self.cells:
            for cell in row:
                print(cell.symbol, end="  ")
            print()

    @staticmethod
    def getWinningIndexes():
        return [Board.rowWinningIndexes(),
                Board.colWinningIndexes(),
                Board.diagWinningIndexes()]

    @staticmethod
    def rowWinningIndexes():
        rowWinningIndexes = []
        for r in range(3):
            rowWinningIndexes.append([(r, c) for c in range(3)])
        return rowWinningIndexes

    @staticmethod
    def colWinningIndexes():
        colWinningIndexes = []
        for c in range(3):
            colWinningIndexes.append([(r, c) for r in range(3)])
        return colWinningIndexes

    @staticmethod
    def diagWinningIndexes():
        return [[(i, i) for i in range(3)], [(i, 3 - 1 - i) for i in range(3)]]

    def isBoardFull(self):
        for row in self.cells:
            for cell in row:
                if cell.symbol != 'x' and cell.symbol != 'o':
                    return False
        return True

    def setCell(self, i, j, symbol):
        if self.cells[i][j].isMarked():
            return False, "Position occupied."
        self.cells[i][j].symbol = symbol
        return True, "Cell marked."

    def getCell(self, i, j):
        return self.cells[i][j].symbol

    def isWinningStateReached(self):
        if self.isBoardFull():
            return (False, 'DRAW')

        for indexList in self.winningIndexes:
            for state in indexList:
                i1, j1 = state[0] 
                i2, j2 = state[1] 
                i3, j3 = state[2] 
                
                if self.cells[i1][j1].symbol == self.cells[i2][j2].symbol == self.cells[i3][j3].symbol == 'x':
                    return (True, 'x')
                elif self.cells[i1][j1].symbol == self.cells[i2][j2].symbol == self.cells[i3][j3].symbol == 'o':
                    return (True, 'o')
        return (False, None)        


