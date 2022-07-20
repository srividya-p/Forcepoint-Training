class Cell:
    def __init__(self, symbol) -> None:
        self.symbol = symbol

    def isMarked(self) -> bool:
        return self.symbol == 'x' or self.symbol == 'o'
