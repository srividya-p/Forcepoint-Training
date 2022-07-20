from card import Card
import random

class Deck:
    suites = ['H', 'C', 'S', 'D']
    cardSymbols = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
    
    def __init__(self, cards) -> None:
        self.undrawnCards = cards
        self.drawnCards = []

    @staticmethod
    def createDeck():
        cards = []
        for suite in Deck.suites:
            for cardSymbol in Deck.cardSymbols:
                cards.append(Card(suite, cardSymbol))
        print(f"{len(cards)} cards added to Deck.")
        return Deck(cards)

    def drawCard(self):
        card = random.choice(self.undrawnCards)
        self.undrawnCards.remove(card)
        self.drawnCards.append(card)
        return card