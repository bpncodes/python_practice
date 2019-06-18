import random

suits=('clubs','diamonds','spades','hearts')
ranks=('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values={'two':1,'three':2,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}

# This is for creating a card obeject
class Card():
	def __init__(self,suit,rank):
		self.suit=suit
		self.rank=rank
	def __str__(self):
		return self.rank+'of'+self.suit

# This is for creation of a new deck 
# Use it once to create a initial deck of 52 cards
class Deck():
	def __init__(self):
		self.deck=[]
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))
	def __str__(self):
		cards_string=''
		for card in self.deck:
			cards_string += card.__str__()
		return cards_string
	def pick_card(self):
		return self.deck.pop()
	def shuffle(self):
		random.shuffle(self.deck)

class Hand():
	def __init__(self,deck):
		self.value=0
		self.cards_in_hand=[]
		self.aces=0
	def pick_card(self):
		single_card=deck.pick_card()
		self.cards_in_hand.append(single_card)
		self.value += values[single_card.rank]
		if single_card.rank == 'ace':
			self.aces += 1	
		

	def adjust_ace(self): 							# This will adjust the value for ace and if the value is above 21 and you have ace then the value 
		while self.aces > 0:								# will be deducted by 10
			if self.value > 21:
				print('Ace adjusted : value decreased by 10 ')
				self.value -= 10
				self.aces -= 1

#Easier method to create a stack of chips 
class Chips():
	def __init__(self,total_chips=100):
		self.total_chips=total_chips
		self.bet=0
	def win_bet(self):
		self.bet += self.total_chips
	def lose_bet(self):
		self.bet -= self.total_chips

#Functions for taking bet
def take_bet(chips): 
	while True :
		try :
			chips.bet=int(input('Enter the amount of bet : '))
		except :
			print('Incorrect input ! Try again')
		else:
			if (chips.total_chips<chips.bet):
				print(f'You have {chips.total_chips} please enter less than that')
				continue
			print('You have sucessfully placed bet')
			break

def player_wins(chips):
	chips.win_bet()

def player_lose(chips):
	chips.lose_bet()

# For showing of cards 0
def show_some(player,dealer):
	print('Player has : ')
	for card in player.cards_in_hand:
		print(card)
	print('The total player value is : ',player.value)
	print('Dealer has : ')
	print(dealer.cards_in_hand[0])
	print('<- Card hidden ->')

# To show all the cards
def show_all(player,dealer):
	print('Player has : ')
	for card in player.cards_in_hand:
		print(card)
	print('The total player value is : ',player.value)
	print('Dealer has : ')
	for card in dealer.cards_in_hand:
		print(card)
	print('The total dealer value is : ',dealer.value)

def hit(player):
		player.pick_card()
		player.adjust_ace()

def hit_or_stand(deck,player):
	while True:
		ip=input('Do you want to hit ? y or n : ')
		if ip[0].lower() == 'y':
			hit(player)
			print('The cards are : ')
			show_some(player,dealer)
		elif ip[0].lower() == 'n':
			print('You have stood : ')
			print('The cards are : ')
			show_some(player,dealer) 
			break
		else:
			print('Incorrect input: Enter again ')
			continue
# The main game

while True:
	print('Welcome to blackjack ! ')
	deck=Deck()
	player=Hand(deck)
	dealer=Hand(deck)
	deck.shuffle()
	chips=Chips()
	player.pick_card()
	player.pick_card()
	dealer.pick_card()
	dealer.pick_card()
	show_some(player,dealer)
	print('How much do you want to bet : ')
	take_bet(chips)
	hit_or_stand(deck,player)
	player_not_already_lose=True
	if player.value > 21 :
		print('You lose dealer wins : ')
		player_lose(chips)
		player_not_already_lose=False
	else:
		while player.value > dealer.value :
			hit(dealer)
	if player_not_already_lose:
		if dealer.value > player.value and dealer.value <= 21 :
			show_all(player,dealer)
			print('Dealer wins you lose : ')
			player_lose(chips)
		elif dealer.value > 21 :			
			player_wins(chips)
			show_all(player,dealer)
			print('Dealer loses you win : ')
		elif dealer.value == player.value :
			show_all(player,dealer)
			print('Its a draw')
	wanna_play_again=input('Wanna play again ? : y or n')
	if wanna_play_again[0].lower() == 'y':
		continue
	else:
		break






