from random import shuffle

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['One', 'Two', 'Three',
        'Four', 'Five', 'Six', 
        'Seven', 'Eight', 'Nine', 'Ten', 
        'Jack', 'Queen', 'King', 'Ace']
values = {'One': 1, 'Two': 2, 'Three': 3, 
        'Four': 4, 'Five': 5, 'Six': 6, 
        'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 
        'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]}

class Deck():

    def __init__(self):
        self.all_cards = []

    def build_deck(self):
        for rank in ranks:
            for suit in suits: 
                new_card_value = (values[rank])
                new_card = Card(rank, suit, new_card_value)
                self.all_cards.append(new_card)

    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        pass

    def __str__(self):
        return str(self.all_cards)
    
class Card():
    
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.rank + ' of ' + self.suit + ': ' + str(self.value)

class Dealer():
    pass

class Player():

    def __init__(self, bank, hand):
        self.bank = bank
        self.hand = []

def main():

    new_deck = Deck()
    
    for rank in ranks:
        for suit in suits: 
            new_card_value = (values[rank])
            new_card = Card(rank, suit, new_card_value)
            new_deck.all_cards.append(new_card)

    new_deck.build_deck()

    for card in new_deck.all_cards:
        print(card)

    print(type(new_deck))

if __name__ == '__main__':
    main()