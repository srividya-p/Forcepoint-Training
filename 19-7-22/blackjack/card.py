class Card:
    pointMap = {'A': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 10, 'K': 10}
    
    def __init__(self, suite, cardSymbol) -> None:
        self.suite = suite
        self.cardSymbol = cardSymbol

    def getCardPoints(self):
        return Card.pointMap[self.cardSymbol]