from operator import ne

class Player:
    def __init__(self, userName) -> None:
        self.userName = userName
        self.points = 0
        self.currentChoice = ''

    def updatePoints(self, card):
        newPoints = card.getCardPoints()
        
        if card.cardSymbol == 'A':
            newPoints = self.decideAcePoints()
        
        self.points += newPoints
        return card

    def decideAcePoints(self):
        return 1 if 11 + self.points > 21 else 11

    def getPoints(self):
        return self.points

    def getUsername(self):
            return self.userName