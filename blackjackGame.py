import random

suites = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'King', 'Queen', 'Jack', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'King':10,
          'Queen':10, 'Jack':10, 'Ace':11}

playing = True


class Card:
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suite


class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suite in suites:
            for rank in ranks:
                self.deck.append(Card(suite, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []     # start with an empty list of cards in player's hand
        self.value = 0      # total sum of cards' value in player's hand
        self.aces = 0       # number of aces in player's hand

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # If total value of cards in Player's hand > 21, consider available ACE values as 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:    # To track the ACCOUNT BALANCE of the player
    def __init__(self, total=100):
        self.total = total      # Default Account Value of the player is 100
        self.bet = 0            # The amount/chips put on bet by the player

    def win_bet(self):          # When player wins the bet amount
        self.total += self.bet

    def lose_bet(self):         # When player loses the bet amount
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except TypeError:
            print('Input an integer value: ')
        else:
            if chips.bet > chips.total:
                    print('Not enough chips. You have {} chips'.format(chips.total))
                    continue
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s :')

        if x[0] == 'h':
            hit(deck, hand)
        elif x[0] == 's':
            print("Player Stands. Dealer's turn.")
        else:
            print('Incorrect input. Enter h or s Only!')
            continue
        break


def player_busts(player,dealer,chips):
    print('Player Busts!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Player Wins!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('Dealer Busts! Player Wins!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('Dealer Wins!')
    chips.lose_bet()


def push():
    print('Player and Dealer Tie ! PUSH')


def show_some(player,dealer):
    print("DEALER'S HAND")
    print('One card is hidden!')
    print(dealer.cards[1])
    print('\n')
    print("PLAYER'S HAND")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print("DEALER'S HAND")
    for card in dealer.cards:
        print(card)
    print('\n')
    print("PLAYER'S HAND")
    for card in player.cards:
        print(card)


# Start the game
print('WELCOME TO BLACKJACK !')

# Create and shuffle the deck. Deal two cards for each player
deck = Deck()
deck.shuffle()

player_hand = Hand()
dealer_hand = Hand()

player_hand.add_card(deck.deal())
player_hand.add_card(deck.deal())

dealer_hand.add_card(deck.deal())
dealer_hand.add_card(deck.deal())

# Set up the Player's chips
player_chips = Chips()

# Prompt the Player for a bet
take_bet(player_chips)

# Show cards, but keep one dealer card hidden
show_some(player_hand, dealer_hand)

while playing:
    # Prompt the Player for Hit or Stand
    hit_or_stand(deck, player_hand)

    # Show cards, but keep one dealer card hidden
    show_some(player_hand, dealer_hand)

    # If Player's hand exceeds 21, player busts and exits the loop
    if player_hand.value > 21:
        player_busts(player_hand, dealer_hand, player_chips)
        break

    # If Player has not busted, play Dealer's hand until Dealer reaches Player's hand value
    if player_hand.value < 21:
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)

        # Show all cards
        show_all(player_hand,dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push()

    # Inform Player of their chips total
    print("Player Chips ar at: {}".format(player_chips.total))

    # Ask to play again
    new_game = input("Do you want to play again? y/n")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing !')
        break


