Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def up_low(s):
	li=list(s)
	up,low=0,0
	for i in li:
		flag=i.isupper()
		if flag:
			up+=1
		else:
			low+=1
	return up,low

>>> up_low('bipin')
(0, 5)
>>> up_low('BiPin')
(2, 3)
>>> 
