from player import Player
from deck import Deck

class Game:
    def __init__(self, playerA = Player('player1'), playerB = Player('player2')):
        self.playerA = playerA
        self.playerB = playerB
        self.deck = Deck.createDeck()
        self.turn = 'A'

    def isWinningStateReached(self):
        if self.playerA.getPoints() == 21:
            return True, self.playerA.getUsername()

        if self.playerB.getPoints() == 21:
            return True, self.playerA.getUsername()

        if self.playerA.getPoints() > 21:
            return True, self.playerB.getUsername()

        if self.playerB.getPoints() > 21:
            return True, self.playerA.getUsername()

        if self.playerA.currentChoice == self.playerB.currentChoice == 's':
            if self.playerA.getPoints() == self.playerB.getPoints():
                return True, 'no one. DRAW'

            return ((True, self.playerA.getUsername()) if self.playerA.getPoints() > self.playerB.getPoints() 
                        else (True, self.playerB.getUsername))

        return False, None

    def startGame(self):
        isGameEnd, winner = False, None
        while not isGameEnd:
            if self.turn == 'A':
                self.playerA.currentChoice = input("Player A choice = ")
                if self.playerA.currentChoice == 's':
                    pass
                elif self.playerA.currentChoice == 'd':
                    card = self.playerA.selectCard(self.deck)
                    print(f"{card.cardSymbol} of {card.suite} was drawn.")
                else:
                    print('Invalid choice.')
            elif self.turn == 'B':
                self.playerB.currentChoice = input("Player B choice = ")
                if self.playerB.currentChoice == 's':
                    pass
                elif self.playerB.currentChoice == 'd':
                    card = self.playerB.selectCard(self.deck)
                    print(f"{card.cardSymbol} of {card.suite} was drawn.")
                else:
                    print('Invalid choice.')
            
            self.turn = 'B' if self.turn == 'A' else 'A'
            print(f"Score A={self.playerA.getPoints()} B={self.playerB.getPoints()}\n")
            isGameEnd, winner = self.isWinningStateReached()

        print(f"Winner is {winner}")

g = Game()
g.startGame()
                
            
        
                    
