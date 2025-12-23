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
        card_to_deal = self.all_cards[0]
        self.all_cards.pop(0)
        return card_to_deal

    def __str__(self):
        return str(self.all_cards)
    
class Card():
    
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    #remove value from return
    def __str__(self):
        return self.rank + ' of ' + self.suit + ': ' + str(self.value)

class Dealer():
    
    def __init__(self):
        self.hand = []

    def hit(self):
        pass

class Player():

    bank_amount = 500

    def __init__(self, bank_amount = 500):
        self.hand = []
        self.bank_amount = bank_amount

    def bet(self):

        while True:
            try:
                bet_amount = int(input('How much would you like to bet? '))

            except ValueError:
                print('That is not a valid input...')
                print('I will ask again.\n')
                continue

            if 0 < bet_amount <= self.bank_amount:
                self.bank_amount -= bet_amount
                print('You have bet: $' + str(bet_amount))
                print('Your new balance is: $' + str(self.bank_amount) + '\n')
                return bet_amount
            elif bet_amount > self.bank_amount:
                print('You do not have enough money to bet that amount.')
                print('Try again...\n')
            elif bet_amount <= 0:
                print('You must bet a positive value.')
                print('Try again...\n')

def main():

    game_on = True
    new_deck = Deck()
    black_jack = 21
    acceptable_choices =  ['Y', 'N']
    player_choice = ''
    the_dealer = Dealer()
    dealer_total = 0
    player = Player()
    player_total = 0
    
    for rank in ranks:
        for suit in suits: 
            new_card_value = (values[rank])
            new_card = Card(rank, suit, new_card_value)
            new_deck.all_cards.append(new_card)

    new_deck.build_deck()
    new_deck.shuffle()


    current_bet = player.bet()

    for _ in range(2):
       player.hand.append(new_deck.deal_one())
    
    print("Player's Cards: ")
    for card in player.hand:
        print(card)
        player_total += card.value
    print('Total: ' + str(player_total))
    print('\n')

    for _ in range(2):
        the_dealer.hand.append(new_deck.deal_one())

    #only show one of dealer's cards
    print("The Dealer's Cards: ")
    for card in the_dealer.hand:
        print(card)
        dealer_total += card.value
    print('\n')

    while player_total < black_jack:
        while player_choice not in acceptable_choices:
            player_choice = input('Would you like to hit (Y or N)? ')
            print('\n')
            if player_choice == 'Y':
                player.hand.append(new_deck.deal_one())
                print("Player's Cards: ")
                for card in player.hand:
                    print(card)
                    player_total += card.value
                print('Total: ' + str(player_total))
                print('\n')
            elif player_choice == 'N':
                break
            else: 
                print('That was not a valid answer. Try again...')
            
            

if __name__ == '__main__':
    main()