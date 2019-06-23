Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def prime(n):
	for i in range(2,n+1):
		for j in range(2,i+1):
			if i % j == 0:
				if i == j :
					yield i
				break

			
>>> list(prime(20))
[2, 3, 5, 7, 11, 13, 17, 19]
>>> #The above gives the prime numbers upto n inclusively
>>> #We test if the number can be divided and if that is the same number then only we make it prime
>>> 


def prime(n):
	for i in range(1,n+1):
		for j in range(2,i):
			if i % j == 0:
				break
		else:
			print(i)
			a=input('Do you want another prime number ? : y or n')
			if a[0].lower() == 'y':
					pass  #This works as well as continue as both of them just goto the next iteration
			else:
					return