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
>>> s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
>>> up_low(s)
(4, 44)
>>> s
'Hello Mr. Rogers, how are you this fine Tuesday?'
>>> up_low('Hello Mr. Rogers, how are you this fine Tuesday')
(4, 43)
>>> def up_low(s):
	li=list(s)
	print(li)
	up,low=0,0
	for i in li:
		flag=i.isupper()
		if flag:
			up+=1
		else:
			low+=1
	return up,low

>>> up_low('Hello Mr. Rogers, how are you this fine Tuesday')
['H', 'e', 'l', 'l', 'o', ' ', 'M', 'r', '.', ' ', 'R', 'o', 'g', 'e', 'r', 's', ',', ' ', 'h', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', ' ', 't', 'h', 'i', 's', ' ', 'f', 'i', 'n', 'e', ' ', 'T', 'u', 'e', 's', 'd', 'a', 'y']
(4, 43)
>>> def up_low(s):
	li=list(s)
	up,low=0,0
	for i in li:
		flag=i.isupper()
		if flag:
			up+=1
		elif:
			i==' '
		else:
			low+=1
	return up,low
SyntaxError: invalid syntax
>>> def up_low(s):
	li=list(s)
	up,low=0,0
	for i in li:
		flag=i.isupper()
		if flag:
			up+=1
		elif i==' ':
			continue
		else:
			low+=1
	return up,low

>>> up_low('Hello Mr. Rogers, how are you this fine Tuesday')
(4, 35)
>>> up_low(s)
(4, 36)
>>> def up_low(s):
	li=list(s)
	up,low=0,
	for i in li:
		if i>='a' and i<='z' or i>='A' and i<='Z':
			flag=i.isupper()
			if flag:
				up+=1
			elif i==' ':
				continue
			else:
				low+=1
	return up,low

>>> up_low(s)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    up_low(s)
  File "<pyshell#26>", line 3, in up_low
    up,low=0,
ValueError: not enough values to unpack (expected 2, got 1)
>>> def up_low(s):
	li=list(s)
	up,low=0,0
	for i in li:
		if i>='a' and i<='z' or i>='A' and i<='Z':
			flag=i.isupper()
			if flag:
				up+=1
			elif i==' ':
				continue
			else:
				low+=1
	return up,low

>>> up_low(s)
(4, 33)
>>> 
