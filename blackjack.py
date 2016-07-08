from random import randint

allSuits = ["DI","SP","HRT","CLUB"]
allValues = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

class Card:
    def __init__(self):
        self.suit =  3
        self.value = 1
    def __init__(self, suit, value):
        self.suit =  int(suit) #allSuits[suit % 4]
        self.value = int(value) 

    def getVal(self):
        value = int(self.value) + 1
        if (self.value >= 10):
            value = 10
        return value

    def printSelf(self):
        print allValues[self.value] + " " + allSuits[self.suit]

                        
class Deck: 
    def __init__(self):
        self.cards = [0] * 52
    
    def exists(self, suit, value):
        if (self.cards[(int(suit) % 4) * 13 + (int(value))] == 1):
            return True
        else:
            return False

    def deal(self, suit, value):
        self.cards[(int(suit)%4) * int(13) + int(value)] = 1

class Player:
    def __init__(self):
        self.cards = 0
        self.cardlist  = []
        self.wins = 0
        self.ace = 0

    def getCard(self, card):
        self.cardlist.append(card)
        self.cards = self.cards + 1
        if card.getVal() == 1:
            print "got an ace"
            self.ace = 1

    def clearCard(self):
        self.cards = 0
        self.cardlist = []

    def cardsInHand(self):
        return self.cards

    def handValue(self):
        sum = 0
        for i in self.cardlist:
            sum = sum + (i.getVal())
        if self.ace == 1 and ((sum+10) <= 21):
            return (sum+10)
        return sum

    def printHand(self):
        for i in self.cardlist:
            i.printSelf()
            



def main():
    a =  Deck()
    startPlayer = randint(0,1)
    players = []
    player1 = Player()
    player2 = Player()
    players.append(player1)
    players.append(player2)
    
    print players[0].cards
    print players[1].cards
    newDeck = Deck()
    for i in players:
        print "PLAYER " + str(players.index(i))
        print "================================="
        suit = randint(0,3)
        value = randint(0,12)
        while (i.cardsInHand() < 2):
            check = newDeck.exists(suit,value)
            while check:
                suit = randint(0,3)
                value = randint(0,12)
                check = newDeck.exists(suit,value)

            newDeck.deal(suit,value)
            newCard = Card(suit,value)
            i.getCard(newCard)

        stayChoice = 0
        while (i.handValue() < 21 and stayChoice == 0):
            print "Your hand is: "
            i.printHand()
            print "Hand value is: " + str(i.handValue())
            if (i.handValue() > 21):
                print "========================="
                print "=========BUST============"
                print "========================="
            elif (i.handValue() == 21):
                print "$$$$$$$$$$$$$$$$$$$$$$$$$"
                print "$$$$$  BLACKJACK  $$$$$$$"
                print "$$$$$$$$$$$$$$$$$$$$$$$$$$"
            else:
                choice = raw_input("hit / stay\n");
                if choice == "hit":
                    print "hit..."
                    suit = randint(0,3)
                    value = randint(0,12)
                    check = newDeck.exists(suit,value)
                    while check:
                        suit = randint(0,3)
                        value = randint(0,12)
                        check = newDeck.exists(suit,value)

                    newDeck.deal(suit,value)
                    newCard = Card(suit,value)
                    i.getCard(newCard)
                    print "Dealt a " 
                    newCard.printSelf()
                else:
                    print "staying..."
                    stayChoice = 1


        if (i.handValue() > 21):
            print "========================="
            print "=========BUST============"
            print "========================="
        elif (i.handValue() == 21):
            print "$$$$$$$$$$$$$$$$$$$$$$$$$"
            print "$$$$$  BLACKJACK  $$$$$$$"
            print "$$$$$$$$$$$$$$$$$$$$$$$$$$"
        else:
            print "Hand value is: " + str(i.handValue())
            print "Hand value is: " + str(i.handValue())
            print "Hand value is: " + str(i.handValue())

        print "\n"
        print "\n"

    print "Player 0 hand value is: " + str(players[0].handValue())
    print "Player 1 hand value is: " + str(players[1].handValue())


    if players[0].handValue() > 21 and players[1].handValue() > 21:
        print "Push! It's a tie."
    elif players[0].handValue() > 21:
        print "Player 1 wins!"
    elif players[1].handValue() > 21:
        print "Player 0 wins!"
    elif players[0].handValue() < 22 and players[1].handValue() < 22:     
        if players[0].handValue() > players[1].handValue():
            print "Player 0 wins"
        else:     
            print "Player 1 wins"
    elif players[0].handValue() == players[1].handValue():
        print "Push! It's a tie."



if __name__ == "__main__":
    main()