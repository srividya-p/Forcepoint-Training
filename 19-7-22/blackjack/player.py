from operator import ne

class Player:
    def __init__(self, userName) -> None:
        self.userName = userName
        self.points = 0
        self.currentChoice = ''

    def selectCard(self, deck):
        card = deck.drawCard()
        newPoints = card.getCardPoints()
        
        if card.cardSymbol == 'A':
            newPoints = self.decideAcePoints()
        
        self.updatePoints(newPoints)
        return card

    def updatePoints(self, newPoints):
        self.points += newPoints

    def decideAcePoints(self):
        return 1 if 11 + self.points > 21 else 11

    def getPoints(self):
        return self.points

    def getUsername(self):
            return self.userName