import random as r

class card:
    def __init__(self, suitNumber):
      self.i = suitNumber

deck = []
for x in range(1,14):
  deck.append(card([x,'of Spades']))
  deck.append(card([x,'of Hearts']))
  deck.append(card([x,'of Diamonds']))
  deck.append(card([x,'of Clubs']))


def display(hand):
  print("This is your hand:")
  i = 1
  for card in hand:
    print(card.i)
    i += 1

def deal(deck):
  hand = []
  ehand = []
  for x in range(3):
    hand = draw(hand,deck)
    ehand = draw(ehand,deck)
  return hand,ehand
pass

def play(deck=deck):
	hand,ehand = deal(deck)
	hand = sorted(hand, key = lambda hand:hand.i[0])
	display(hand)
	drawChoice = input("Do you want to draw a card Y/N")
	if drawChoice == "Y":
		draw(hand,deck)
		oppsum(ehand)
		sum(hand)
		if oppsum <= 17:
			edraw(ehand,deck)
			print("Opponent draws a card")
		if abs(A)>abs(B):
			print("You Win!")
		else:
			print("You Lose :(")
	else:
		oppsum(ehand)
		sum(hand)
		if oppsum <= 17:
			edraw(ehand,deck)
			print("Opponent draws a card")
		if abs(A)>abs(B):
			print("You Win!")
		elif abs(A)<abs(B):
			print("You Lose :(")

#display(ehand)

def draw(hand,deck):
  hand.append(deck.pop(r.randint(0,len(deck)-1)))
  return hand
  display(hand)

def edraw(ehand,deck):
  ehand.append(deck.pop(r.randint(0,len(deck)-1)))
  return ehand
  display(hand)

def display(hand):
  print("This is your hand:")
  i = 1
  for card in hand:
    print(card.i)
    i += 1

def sum(hand):
	sum = 0
	global B
	for card in hand:
	 sum += card.i[0]
	print("Your hand number:")
	print(sum)
	B = 21 - sum

def oppsum(ehand):
	global A
	global oppsum
	oppsum = 0
	for card in ehand:
	 oppsum += card.i[0]
	print("Your opponent's hand number:")
	print(oppsum)
	A = 21 - oppsum
play()




