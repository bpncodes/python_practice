import email.utils
import string
def f():
	lower=string.ascii_lowercase
	upper=string.ascii_uppercase
	a=input('enter ')
	val=0
	i=a[val]
	leng=len(a)-1
	#This will check it till the first USERNAME
	while i!='@':
		try:
			if i in lower or  i in upper or type(int(i))==int or i=='_' or i=='-':
				if val==leng:
					print('Out of range')
					return
				val += 1
				i=a[val]
			else:
				print('Not Valid USERNAME')
				break
		except:
			print('Invalid char in USERNAME. Exiting program ...')
			return
	
	print('USERNAME passed')
	i = a[val + 1]
	#This is for checking domain
	while i!='.':
		if i in lower:
			if val==leng:
				print('Out of range ')
				return
			val += 1
			i = a[val]
		else:
			print('Not valid domain')
			return

	print('Domain Passed')

	#This is for checking the extension
	val+=1
	count=0
	i=a[val]
	while val <= leng:
		if i in lower:
			count+=1
			val+=1
			i=a[val]
			if val==leng:
				if i in lower:
					count+=1
					break
				else:
					print('End of char in extension')
					return
		else:
			print('Not valid extension')
			return
	if count<4:
		print('Valid extension')
	else:
		print('Invalid extension')
		return
	print('Valid email')
f()