import random

class Playing_Cards:
    def __init__(self):
        self.deck = []
        self.make_cards()

    def make_cards(self):
        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        types = ['C', 'D', 'H', 'S']
        i = 0
        while i < len(types):
            for card in cards:
                card += types[i]
                self.deck.append(card)
            i += 1
        print(self.deck)

    def shuffle(self):
        for i in range(len(self.deck)):
            idx = random.randint(0, len(self.deck) - 1)
            # print(idx)
            swapped_card = self.deck[idx]
            self.deck[idx] = self.deck[i]
            self.deck[i] = swapped_card

        print(len(set(self.deck)) == len(self.deck))
        print(self.deck)

deck1 = Playing_Cards()
deck1.shuffle()
