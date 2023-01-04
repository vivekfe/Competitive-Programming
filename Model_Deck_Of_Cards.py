
suits=('Hearts', 'Diamonds', 'Spades', 'Clubs')
picture_cards_to_rank = {'Ace':13, 'King':12, 'Queen':11, 'Jack':10}
class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value= value

    def __str__(self):
        return f'Suit: {self.suit} Value: {self.value} Rank in suit: {self.rank}'

    def __repr__(self):
        return f'Suit: {self.suit} Value: {self.value} Rank in suit: {self.rank}'

class deck_of_cards:
    def __init__(self):
        self.deck= list()  # want to maintain order of cards in the desk so not using the set
        for suit in suits:
            print(suit)
            for number_card in range(2,10):
                self.deck.append(Card(rank=number_card-1, suit=suit, value=number_card))
            for picture_card in picture_cards_to_rank:
                self.deck.append(Card(rank=picture_cards_to_rank[picture_card], suit=suit, value=picture_card))

    def __str__(self):
        card_deck_string = ""
        for card in self.deck:
            card_deck_string = card_deck_string + f'Card: {card}\n'
        return card_deck_string

my_card_deck = deck_of_cards()
print(my_card_deck)
{k:v for k,v in sorted(picture_cards_to_rank.items(), key= lambda item:item[1])}
