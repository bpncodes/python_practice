Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def printit():
	for i in range(1,12):
		for j in range(1,12):
			if i==2 and j==2:
					print('A',end='')
			elif i==2 and j==6:
					print('B',end='')
			elif i==2 and j==10:
					print('C',end='')
			elif i==6 and j==2:
					print('D',end='')
			elif i==6 and j==6:
					print('E',end='')
			elif i==6 and j==10:
					print('F',end='')
			elif i==10 and j==2:
					print('G',end='')
			elif i==10 and j==6:
					print('H',end='')
			elif i==10 and j==10:
					print('I',end='')
			elif (i%4==0) and (j%4==0):
					print(' ',end='')
			elif i%4==0 and j%4!=0:
					print('-',end='')
			elif i%4!=0 and j%4==0:
					print('|',end='')
			elif i%4!=0 and j%4!=0:
					print(' ',end='')
		print('\n')

		
>>> 
