Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class BankAccount():
	def __init__(self,name='Not assigned',balance=0):
		self.name=name
		self.balance=balance
	def __str__(self):
		return(f'Account owner: {self.name}\nAccount balance: ${str(self.balance)}')
	def deposite(self,deposite_amount):
		self.balance+=deposite_amount
		print(f'Amount of {deposite_amount} deposited')
		print(f'Account balance: ${self.balance}')
	def withdraw(self,withdraw_amount):
		if withdraw_amount<self.balance:
			self.balance-=withdraw_amount
			print(f'Amount of {withdraw_amount} withdrawn sucessfully')
			print(f'Account balance: ${self.balance}')
		else:
			print(f'Please enter a amount less than {self.balance}')

			
>>> myac=BankAccount('Bipin',100)
>>> print(myac)
Account owner: Bipin
Account balance: $100
>>> myac.deposite(10)
Amount of 10 deposited
Account balance: $110
>>> myac.withdraw(40)
Amount of 40 withdrawn sucessfully
Account balance: $70
>>> myac.withdraw(1000)
Please enter a amount less than 70
>>> 
