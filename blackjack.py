#Blackjack Game 
#Started 2.7.14
#Finished 2.10.14

import random

#Classes
class Card(object):
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def display(self):
        return self.suit + str(self.value)
    
class Hand(object):

    def __init__(self, hand):
        self.hand = hand
        
    def total(self):
        total = 0
        for x in self.hand:
            if x.value in [10, 11, 12, 13]:
                total += 10
            if x.value in [2, 3, 4, 5, 6, 7, 8, 9]:
                total += x.value
        for y in self.hand:
            if y.value == 1:
                if total <= 10:
                    total += 11
                else:
                    total += 1
        return total
    
    def display(self):
        hand = []
        for x in self.hand:
            hand.append(x.display())
        return hand
        
    def hit(self, deck):
        if len(deck) >= 1:
            self.hand.append(deck[0])
            deck = remove_card(self.hand[-1], deck)
        else:
            deck = shuffle_deck(create_deck(deck))
            self.hand.append(deck[0])
            deck = remove_card(self.hand[-1], deck)
        return deck

#1.0 Make Deck
deck = []
def create_deck(deck):
    for a in ["H", "D", "S","C"]:
        for i in range(1,14):
            item = Card(a, i)
            deck.append(item)
    return deck
deck = create_deck(deck)

def remove_card(card, deck):
    n = deck.index(card)
    if int(n) == 0:
        new_deck = deck[1:]
    else:
        new_deck = deck[0:n] + deck[n+1:]
    return new_deck

#2.0 Shuffle Deck
def shuffle_deck(deck):
    shuffled = []
    old_deck = deck
    while len(shuffled) != 52:
        card = random.choice(old_deck)
        shuffled.append(card)
        remove_card(card, old_deck)
    return shuffled
deck = shuffle_deck(deck)

#3.0 Deal Hand
def new_deal(deck):
    current_deck = deck
    if len(current_deck) > 4:
        player = [deck[0], deck[1]]
        computer = [deck[2], deck[3]]
        current_deck = current_deck[4:]
    elif len(current_deck) == 4:
        player = [deck[0], deck[1]]
        computer = [deck[2], deck[3]]
        current_deck = shuffle_deck(create_deck(current_deck))
    elif len(current_deck) == 3:
        player = [deck[0], deck[1]]
        computer = [deck[2]]
        current_deck = shuffle_deck(create_deck(current_deck))
        computer.append(deck[0])
        current_deck = current_deck[1:]
    elif len(current_deck) == 2:
        player = [deck[0], deck[1]]
        current_deck = shuffle_deck(create_deck(current_deck))
        computer = [deck[0], deck[1]]
        current_deck = current_deck[2:]
    elif len(current_deck) == 1:
        player = [deck[0]]
        current_deck = shuffle_deck(create_deck(current_deck))
        player.append(deck[0])
        computer = [deck[1], deck[2]]
        current_deck = current_deck[3:]
    elif len(current_deck) == 0:
        current_deck = shuffle_deck(create_deck(current_deck))
        player = [deck[0], deck[1]]
        computer = [deck[2], deck[3]]
        current_deck = current_deck[4:]
    return player, computer, current_deck

#Play Game
print ""
print "Ready for some BLACKJACK!"
play = raw_input("Type 'yes' to play: ")
print ""
while play != "yes":
    play = raw_input("Wait, so do you want to play? Type 'yes' and press Enter: ")
money = 100
print ""
print "Great, you start with $100. Minimum bet is $5."
input_is_correct = False
while not input_is_correct:
    bet = raw_input("Enter your bet here: $")
    try:
        number = int(bet)
        if number >= 5 and number <= 100:
            input_is_correct = True
    except ValueError:
        print "Please enter a number between 5 and 100."
bet = int(bet)
while play == "yes":
    if play == "yes":
        player, computer, deck = new_deal(deck)
    player_hand, computer_hand = Hand(player), Hand(computer)
    money -= bet
    print ""
    print "Your hand :", player_hand.display()
    print "Your total:", player_hand.total()
    print "Your bet  : $" + str(bet)
    print "Dealer has: [ [] , '" + computer[0].display() + "']"
    print ""
    if player_hand.total() == 21:
        print "Congrats! You got Blackjack! Let's see what the dealer got."
        if computer_hand.total() == 21:
            print "The dealer has: ", computer_hand.display()
            print "The dealer got Blackjack too. It's a push."
            money = money + bet
        else:
            print "The dealer has: ", computer_hand.display()
            print "The dealer didn't have Blackjack. You Win!"
            money = money + bet + bet + (0.5 * bet)
    else:
        action = raw_input("Would you like to 'hit' or 'stay'?: ")
        while action not in ["hit", "stay"]:
            action = raw_input("I'm sorry, that's not an option.  Please type 'hit' or 'stay': ")
        while action == "hit":
            deck = player_hand.hit(deck)
            print ""
            print "Your new hand: ", player_hand.display()
            print "Your new total: ", player_hand.total()
            print ""
            if player_hand.total() > 21:
                print "Oh no! You went over 21, Dealer wins this round."
                break
            else:
                action = raw_input("Would you like to 'hit' again or 'stay'?: ")
                while action not in ["hit", "stay"]:
                    action = raw_input("I'm sorry, that's not an option.  Please type 'hit' or 'stay': ")
        if action == "stay":
            #Determine Computer's Score
            print ""
            print "The dealer has: ", computer_hand.display()
            print "Total: ", computer_hand.total()
            while computer_hand.total() <= 16:
                deck = computer_hand.hit(deck)
                print ""
                print "The dealer hit and now has: ", computer_hand.display()
                print "Total: ", computer_hand.total()
            #Determine Winner and Cash Winnings
            print ""
            if computer_hand.total() > 21:
                print "Yay! The dealer went over. You win!"
                money = money + bet + bet
            elif player_hand.total() > computer_hand.total():
                print "Yay! You win!"
                money = money + bet + bet
            elif player_hand.total() == computer_hand.total():
                print "It's a push."
                money = money + bet
            else:
                print "Sorry! Dealer wins."

    print ""
    if money == 0:
        print "Sorry, you ran out of money! Better luck next time!"
        break
    print "You currently have $" + str(money) + "."
    print "Would you like to keep playing?"
    print ""
    play = raw_input("Type 'yes' or type 'cash' to cash out: ")
    while play not in ['yes', 'cash']:
        play = raw_input("Did you mean 'yes' or 'cash'?: ")
    if play == "yes":
        input_is_correct = False
        while not input_is_correct:
            bet = raw_input("Enter your new bet here: $")
            try:
                number = int(bet)
                if number >= 5 and number <= money:
                    input_is_correct = True
            except ValueError:
                print "Sorry, that's not a valid bet. Please enter a number between 5 and $" + str(money) + "."
        bet = int(bet)
        
#Cash Out
if play == "cash":
    if money > 100:
        print ""
        print "Congrats! You leave with $" + str(money) + "."
        print "That means you made $" + str((money - 100)) + "!"
            
    elif money == 100:
        print ""
        print "Good Job! You leave with $" + str(money) + "."
        print "You broke even, meaning you didn't lose any money!"
    
    elif money < 100:
        print ""
        print "Oh no! You leave with $" + str(money) + "."
        print "Better luck next time!"
    
print ""
print "Thanks for playing! :D"
    
    #the end
