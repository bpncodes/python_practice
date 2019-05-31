Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
SyntaxError: invalid syntax
>>> def paper_doll(userip):
	m=[]
	for i in userip:
		m.append(i*3)
	''.join(m)
	return m

>>> paper_doll('Hello')
['HHH', 'eee', 'lll', 'lll', 'ooo']
>>> def paper_doll(userip):
	m=[]
	for i in userip:
		m.append(i*3)
	return ''.join(m)

>>> paper_doll('Hello')
'HHHeeellllllooo'
>>> paper_doll('Mississippi')
'MMMiiissssssiiissssssiiippppppiii'
>>> 
>>> BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'¶

SyntaxError: invalid syntax
>>> def blackjack(n1,n2):
	sum=n1+n2
	if sum<=21:
		return sum
	elif sum>21 and n1==11 or n2==11:
		sum=sum-11
		if sum<=21:
			return sum
		else:
			return "bust"
	else:
		return "bust"

	
>>> blackjack(def blackjack(n1,n2,n3):
	sum=n1+n2+n3
	if sum<=21:
		return sum
	elif sum>21 and n1==11 or n2==11 or n3=11:
		sum=sum-11
		if sum<=21:
			return sum
		else:
			return "bust"
	else:
		return "bust"
	  
SyntaxError: invalid syntax
>>> def blackjack(n1,n2,n3):
	sum=n1+n2+n3
	if sum<=21:
		return sum
	elif sum>21 and n1==11 or n2==11 or n3=11:
		sum=sum-11
		if sum<=21:
			return sum
		else:
			return "bust"
	else:
		return "bust"
	
SyntaxError: invalid syntax
>>> def blackjack(n1,n2,n3):
	sum=n1+n2+n3
	if sum<=21:
		return sum
	elif sum>21 and n1==11 or n2==11 or n3==11:
		sum=sum-11
		if sum<=21:
			return sum
		else:
			return "bust"
	else:
		return "bust"

	
>>> blackjack(5,6,7)
18
>>> blackjack(9,9,9) --> 'BUST'
SyntaxError: invalid syntax
>>> blackjack(9,9,9)
'bust'
>>> blackjack(9,9,11)
18
>>> SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.¶

SyntaxError: invalid syntax
>>> 
