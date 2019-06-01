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
>>> def unique_list(lst):
	lst=set(lst)
	print(lst)
	lst=list(set)

	
>>> unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
{1, 2, 3, 4, 5}
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
  File "<pyshell#35>", line 4, in unique_list
    lst=list(set)
TypeError: 'type' object is not iterable
>>> a={1,2,3,4}
>>> a.pop()
1
>>> a.remove(2)
>>> a
{3, 4}
>>> def unique_list(lst):
	lst=set(lst)
	print(lst)

	
>>> unique_list([1,2,3,4])
{1, 2, 3, 4}
>>> unique_list([1,2,3,4,4,4,4,4,4,4,4,3,3,2,3,1,3,4])
{1, 2, 3, 4}
>>> res=unique_list([1,2,3,4,4,4,4,4,4,4,4,3,3,2,3,1,3,4])
{1, 2, 3, 4}
>>> res
>>> re
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    re
NameError: name 're' is not defined
>>> res
>>> def unique_list(lst):
	lst=set(lst)
	print(lst)
	return lst

>>> res=unique_list([1,2,3,4,4,4,4,4,4,4,4,3,3,2,3,1,3,4])
{1, 2, 3, 4}
>>> res
{1, 2, 3, 4}
>>> l=[]
>>> for i in res:
	l.append(i)

	
>>> l
[1, 2, 3, 4]
>>> def unique_list(lst):
	result=[]
	lst=set(lst)
	for i in lst:
		result.append(i)

		
>>> unique_list([1,2,3,4,4,4,4,4,4,4,4,3,3,2,3,1,3,4])
>>> def unique_list(lst):
	result=[]
	lst=set(lst)
	for i in lst:
		result.append(i)
	return result

>>> unique_list([1,2,3,4,4,4,4,4,4,4,4,3,3,2,3,1,3,4])
[1, 2, 3, 4]
>>> '''Write a Python function that checks whether a passed in string is palindrome or not.'''
'Write a Python function that checks whether a passed in string is palindrome or not.'
>>> def pali(string):
	rev=string
	rev=rev[::-1]
	if rev==string
	
SyntaxError: invalid syntax
>>> def pali(string):
	rev=string
	rev=rev[::-1]
	if rev==string:
		print(f'The given string {string} is palindrone')
	else:
		print(f'The given string {string} is not palindrone')

		
>>> pali('bipin')
The given string bipin is not palindrone
>>> pali('helleh')
The given string helleh is palindrone
>>> pali('bipinipib')
The given string bipinipib is palindrone
>>> string
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    string
NameError: name 'string' is not defined
>>> string='bpin'
>>> string=split()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    string=split()
NameError: name 'split' is not defined
>>> string.split()
['bpin']
>>> string
'bpin'
>>> lst(string)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    lst(string)
NameError: name 'lst' is not defined
>>> for i in string:
	print(i)

	
b
p
i
n
>>> for i in string:
	if i in 'karki':
		return True
	
SyntaxError: 'return' outside function
>>> 
>>> for i in string:
	if i in 'karki':
		print('tu')

		
tu
>>> def check(string):
	l=[]
	 for i in string:
		 if i in 'abcdefghijklmnopqrstuvwxyz':
			 l.append(i)
			 
SyntaxError: unexpected indent
>>> def check(string):
	 l=[]
	 for i in string:
		 if i in 'abcdefghijklmnopqrstuvwxyz' and not in l:
			 l.append(i)
			 
SyntaxError: invalid syntax
>>> def check(string):
	 l=[]
	 count=0
	 for i in string:
		 if i in 'abcdefghijklmnopqrstuvwxyz':
			 if i not in l:
				 l.append(i)
				 count+=1
	return count==26
SyntaxError: unindent does not match any outer indentation level
>>> def check(string):
	 l=[]
	 count=0
	 for i in string:
		 if i in 'abcdefghijklmnopqrstuvwxyz':
			 if i not in l:
				 l.append(i)
				 count+=1
	 return count==26

	
>>> check('bipin')
False
>>> check("The quick brown fox jumps over the lazy dog")
True
>>> check('alksdjfl;aksdjfl;askdjfslkjf')
False
>>> check('abcdefghijklmnop')
False
>>> check("The quick brown fox jumps over the lazy dog")
True
>>> def check(string):
	 l=[]
	 count=0
	 for i in string:
		 if i in 'abcdefghijklmnopqrstuvwxyz':
			 if i not in l:
				 l.append(i)
				 count+=1
				 print(l)
	 return count==26

	
>>> check('alksdjfl;aksdjfl;askdjfslkjf')
['a']
['a', 'l']
['a', 'l', 'k']
['a', 'l', 'k', 's']
['a', 'l', 'k', 's', 'd']
['a', 'l', 'k', 's', 'd', 'j']
['a', 'l', 'k', 's', 'd', 'j', 'f']
False
>>> check("The quick brown fox jumps over the lazy dog")
['h']
['h', 'e']
['h', 'e', 'q']
['h', 'e', 'q', 'u']
['h', 'e', 'q', 'u', 'i']
['h', 'e', 'q', 'u', 'i', 'c']
['h', 'e', 'q', 'u', 'i', 'c', 'k']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y', 'd']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y', 'd', 'g']
True
>>> a='slkfjalskd'
>>> a=['a','v
   
SyntaxError: EOL while scanning string literal
>>> a=['a','v','d']
>>> a.sort()
>>> a
['a', 'd', 'v']
>>> def check(string):
	 l=[]
	 count=0
	 for i in string:
		 if i in 'abcdefghijklmnopqrstuvwxyz':
			 if i not in l:
				 l.append(i)
				 count+=1
				 print(l)
	 l.sort()
	 return l

	
>>> check("The quick brown fox jumps over the lazy dog")
['h']
['h', 'e']
['h', 'e', 'q']
['h', 'e', 'q', 'u']
['h', 'e', 'q', 'u', 'i']
['h', 'e', 'q', 'u', 'i', 'c']
['h', 'e', 'q', 'u', 'i', 'c', 'k']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y', 'd']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y', 'd', 'g']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> def check(string):
	 	 l=[]
	 	 count=0
	 	 for i in string:
	 		 if i in 'abcdefghijklmnopqrstuvwxyz':
	 			 if i not in l:
	 				 l.append(i)
	 				 count+=1
	 				 print(l)
	 	 return count==26

	 	
>>> check("The quick brown fox jumps over the lazy dog")
['h']
['h', 'e']
['h', 'e', 'q']
['h', 'e', 'q', 'u']
['h', 'e', 'q', 'u', 'i']
['h', 'e', 'q', 'u', 'i', 'c']
['h', 'e', 'q', 'u', 'i', 'c', 'k']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y', 'd']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y', 'd', 'g']
True
>>> def check(string):
	 l=[]
	 count=0
	 for i in string:
		 if i in 'abcdefghijklmnopqrstuvwxyz':
			 if i not in l:
				 l.append(i)
				 count+=1
				 print(l)
	 print(l.sort())
	 return l

	
>>> check("The quick brown fox jumps over the lazy dog")
['h']
['h', 'e']
['h', 'e', 'q']
['h', 'e', 'q', 'u']
['h', 'e', 'q', 'u', 'i']
['h', 'e', 'q', 'u', 'i', 'c']
['h', 'e', 'q', 'u', 'i', 'c', 'k']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y', 'd']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y', 'd', 'g']
None
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> def check(string):
	 l=[]
	 count=0
	 for i in string:
		 if i in 'abcdefghijklmnopqrstuvwxyz':
			 if i not in l:
				 l.append(i)
				 count+=1
				 print(l)
	 print(l.sort())
	 return count==26

	
>>> check("The quick brown fox jumps over the lazy dog")
['h']
['h', 'e']
['h', 'e', 'q']
['h', 'e', 'q', 'u']
['h', 'e', 'q', 'u', 'i']
['h', 'e', 'q', 'u', 'i', 'c']
['h', 'e', 'q', 'u', 'i', 'c', 'k']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y', 'd']
['h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y', 'd', 'g']
None
True
>>> 
