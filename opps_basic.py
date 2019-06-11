Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Animal():
	def __init__(self,name,breed):
		self.name=name
		self.breed=breed
	def __str__(self):
		return f'My name is {self.name}'
	def __del__(self):
		return f'{self.name} has been deleted}
	
SyntaxError: EOL while scanning string literal
>>> class Animal():
	whatis='animal'
	def __init__(self,name,breed):
		self.name=name
		self.breed=breed
	def __str__(self):
		return f'My name is {self.name}'
	def __del__(self):
		return f'{self.name} has been deleted'
	def makesound(self,sound):
		print(f'The sound is {sound}')

		
>>> dog=Animal()
Exception ignored in: <function Animal.__del__ at 0x03742E88>
Traceback (most recent call last):
  File "<pyshell#11>", line 9, in __del__
AttributeError: 'Animal' object has no attribute 'name'
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    dog=Animal()
TypeError: __init__() missing 2 required positional arguments: 'name' and 'breed'
>>> dog=Animal('Dog','Shephered')
>>> print(dog)
My name is Dog
>>> del dog
>>> dog
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dog
NameError: name 'dog' is not defined
>>> dog=Animal('Dog','Shephered')class Animal():
	whatis='animal'
	def __init__(self,name,breed):
		self.name=name
		self.breed=breed
	def __str__(self):
		return f'My name is {self.name}'
	def __del__(self):
		return f'obj has been deleted'
	def makesound(self,sound):
		print(f'The sound is {sound}')
		
SyntaxError: invalid syntax
>>> 
>>> class Animal():
	whatis='animal'
	def __init__(self,name,breed):
		self.name=name
		self.breed=breed
	def __str__(self):
		return f'My name is {self.name}'
	def __del__(self):
		return f'obj has been deleted'
	def makesound(self,sound):
		print(f'The sound is {sound}')

		
>>> dog
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    dog
NameError: name 'dog' is not defined
>>> dog=Animal('a','a')
>>> del dog
>>> class Animal():
	whatis='animal'
	def __init__(self,name,breed):
		self.name=name
		self.breed=breed
	def __str__(self):
		return f'My name is {self.name}'
	def __del__(self):
		return f'obj has been deleted'
	def makesound(self,sound):
		print(f'The sound is {sound}')

		
>>> dog=Animal('a','a')
>>> print(del dog)
SyntaxError: invalid syntax
>>> a=del dog
SyntaxError: invalid syntax
>>> a=del dog
SyntaxError: invalid syntax
>>> dog
<__main__.Animal object at 0x03733A50>
>>> print(dog)
My name is a
>>> class Animal():
	whatis='animal'
	def __init__(self,name,breed):
		self.name=name
		self.breed=breed
	def __str__(self):
		return f'My name is {self.name}'
	def __del__(self):
		print 'obj has been deleted'
	def makesound(self,sound):
		print(f'The sound is {sound}')
		
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('obj has been deleted')?
>>> 
>>> class Animal():
	whatis='animal'
	def __init__(self,name,breed):
		self.name=name
		self.breed=breed
	def __str__(self):
		return f'My name is {self.name}'
	def __del__(self):
		print('obj has been deleted')
	def makesound(self,sound):
		print(f'The sound is {sound}')

		
>>> dog
<__main__.Animal object at 0x03733A50>
>>> dog=Animal('a','a')
>>> dog
<__main__.Animal object at 0x03749470>
>>> str(dog)
'My name is a'
>>> del dog
obj has been deleted
>>> ab=(1,2)
>>> ab
(1, 2)
>>> x,y=ab
>>> x
1
>>> y
2
>>> x,y,z=ab
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x,y,z=ab
ValueError: not enough values to unpack (expected 3, got 2)
>>> x=ab
>>> x=(3,4,3,5,3,5,3,2)
>>> a,b=x
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a,b=x
ValueError: too many values to unpack (expected 2)
>>> a,*b,c=x
>>> b
[4, 3, 5, 3, 5, 3]
>>> a
3
>>> class Line():
	def __init__(self,c1,c2):
		self.x1,self.y1=c1
		self.x2,self.y2=c2
	def slope(self):
		deltax=self.x2-self.x1
		deltay=self.y2-self.y1
		slope=deltay/deltax
		return slope
	def distance(self):
		deltax=self.x2-self.x1
		deltay=self.y2-self.y1
		sumofboth=deltax**2+deltay**2
		distance=sumofboth**0.2
		return distance

	
>>> line1=(4,2)
>>> line2=(6,4)
>>> li=Line(line1,line2)
>>> li.x1
4
>>> li.slope()
1.0
>>> li.distance()
1.5157165665103982
>>> coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
SyntaxError: multiple statements found while compiling a single statement
>>> line1=(3,2)
>>> line2=(6,4)
>>> li=Line(line1,line2)
>>> li.x1
3
>>> li.distance()
1.6702776523348104
>>> l.slope()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    l.slope()
NameError: name 'l' is not defined
>>> li.slope
<bound method Line.slope of <__main__.Line object at 0x03749390>>
>>> li.slope()
0.6666666666666666
>>> class Line():
	def __init__(self,c1,c2):
		self.x1,self.y1=c1
		self.x2,self.y2=c2
	def slope(self):
		deltax=self.x2-self.x1
		deltay=self.y2-self.y1
		slope=deltay/deltax
		return slope
	def distance(self):
		deltax=self.x2-self.x1
		deltay=self.y2-self.y1
		sumofboth=deltax**2+deltay**2
		distance=sumofboth**0.2
		return distance

	
>>> a=1
>>> b=4
>>> b**2
16
>>> b**0.2
1.3195079107728942
>>> class Line():
	def __init__(self,c1,c2):
		self.x1,self.y1=c1
		self.x2,self.y2=c2
	def slope(self):
		deltax=self.x2-self.x1
		deltay=self.y2-self.y1
		slope=deltay/deltax
		return slope
	def distance(self):
		deltax=self.x2-self.x1
		deltay=self.y2-self.y1
		sumofboth=deltax**2+deltay**2
		distance=sumofboth**0.5
		return distance

	
>>> line1
(3, 2)
>>> line2
(6, 4)
>>> line2=(8,10)
>>> line2
(8, 10)
>>> li=Line(line1,line2)
>>> li.distance()
9.433981132056603
>>> li.slope()
1.6
>>> def
