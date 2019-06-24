import email.utils
import string
def f(mail):
	lower=string.ascii_lowercase
	upper=string.ascii_uppercase
	dash='-._'
	mail=email.utils.parseaddr(mail)
	name , a = mail
	val=0
	i=a[val]
	leng=len(a)-1
	#This will check it till the first USERNAME
	if i in lower or i in upper:
		pass
	else:
		return
	while i!='@':
		try:
			if i in lower or  i in upper or i in dash or type(int(i))==int :
				if val==leng:
					return
				val += 1
				i=a[val]
			else:
				break
		except:
			return
	try:
		val+=1
		i=a[val]
	except:
		return
	#This is for checking domain
	while i!='.':
		if i in lower:
			if val==leng:
				return
			val += 1
			i = a[val]
		else:
			return


	#This is for checking the extension
	val+=1
	count=0
	i=a[val]
	while val <= leng:
		if i in lower:
			
			if val==leng:
				if i in lower:
					count+=1
					break
				else:
					return
			count+=1
			val+=1
			i=a[val]
		else:
			return
	if count<4:
		print(email.utils.formataddr(mail))
	else:
		return

num=int(input())
l=[]
for i in range(num):
	a=input()
	l.append(a)
for i in l:
	f(i)
