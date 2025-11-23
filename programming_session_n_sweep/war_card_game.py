# war game

"""
How to play War

    #DONE Setup: Shuffle a standard 52-card deck and deal the cards face down as evenly as possible to all players. Each player keeps their cards in a face-down stack.

    #DONE Battle: Each player turns the top card of their stack face up at the same time.

    #DONE Win a round: The player with the highest-ranking card wins all the cards in that round. Aces are high, and two is the lowest,
                with suits ignored. The winner places all the won cards at the bottom of their deck.

    The "War":
        If two or more players have cards of the same rank, a war begins. #done
        The tied players each place three cards face down on top of their original card. #done
        They then turn a fourth card face up. #done
        The player with the higher face-up card wins all the cards played in that war, which includes the initial pair and all the face-down and face-up cards. #done
        If the face-up cards in a war also tie, the process repeats with another round of three face-down and one face-up card until a winner is determined. #done

    Winning the game: The game ends when one player has collected all 52 cards


"""
import random

SUITS = ["Spade", "Heart", "Club", "Diamond"]

CARDS_AT_WAR = 3


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return self.__str__()


# card = Card("Spade", 14)

# create deck of cards
all_cards = []

for suit in SUITS:
    for val in range(2, 15):
        all_cards.append(Card(suit, val))

# print(all_cards)


class Deck:

    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):

        return self.cards.pop(0)


deck = Deck(all_cards)

# print(deck.cards)

deck.shuffle()

# print(deck.cards)

# print(deck.draw_card())

# print(len(deck.cards))


class Player:

    def __init__(self, cards=[]):
        self.cards = cards

    def show(self):
        
        return self.cards.pop(0)

    def receive(self, cards):
        random.shuffle(cards)
        self.cards += cards
        
    def has_cards(self,val=1):

        return len(self.cards) >= val




# draw cards
first_half = []
second_half = []


while deck.cards:
    first_half.append(deck.draw_card())
    second_half.append(deck.draw_card())

first_player = Player(first_half)
second_player = Player(second_half)


def print_data():
    print("################ players cards at the beginning ####################")
    print("FIRST PLAYER")
    print(first_player.cards)
    print("SECOND PLAYER")
    print(second_player.cards)


def get_players_cards():
    
    

    return first_player.show(), second_player.show()

table=[]

running = True
while running:

    # player flip both top cards

    if not (first_player.has_cards() and second_player.has_cards()):
        print_data()
        break

    player_1_card, player_2_card = get_players_cards()


    table += [player_1_card, player_2_card]
    

    # compare value of the cards
    if player_1_card.value > player_2_card.value:
        # give all the cards to the first player
        first_player.receive(table)
        table=[]
        print("player 1 wins")

    elif (player_1_card.value == player_2_card.value) and (first_player.has_cards(3) and second_player.has_cards(3) ):
        for _ in range(CARDS_AT_WAR):
            player_1_card, player_2_card = get_players_cards()
            table.append(player_1_card)
            table.append(player_2_card)

        print('tie')
        continue
    else:
        # give the second player all the cards in the table
        second_player.receive(table)
        table=[]
        print("player 2 wins")

