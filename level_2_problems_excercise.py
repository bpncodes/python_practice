Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False

SyntaxError: invalid character in identifier
>>> def has_33(seq):
	n=0
	for i in seq:
		if i==3:
			n+=1
		else:
			n-=1
		if n==2:
			return True
	return False

>>> has_33([1,3,3])
False
>>> def has_33(seq):
	n=0
	val=False
	for i in seq:
		if i==3:
			n+=1
			val=True
		else:
			
			if val:
				n-=1
				val=False
		if n==2:
			return True
	return False

>>> has_33([1,3,3])
True
>>> has_33([1,3,1,3])
False
>>> has_33([3,1,3])
False
>>> has_33([11,2,3,4,5,3,3])
True
>>> 
