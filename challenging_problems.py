Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

SyntaxError: invalid syntax
>>> def summer_69(uinput):
	six,nine=True
	sum=0
	for i in uinput:
		if i==6:
			six=False
		elif i==9:
			six=True	
		elif six and nine:
			sum+=i
		else:
			continue
	return sum

>>> summer_69([1, 3, 5])
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    summer_69([1, 3, 5])
  File "<pyshell#14>", line 2, in summer_69
    six,nine=True
TypeError: cannot unpack non-iterable bool object
>>> def summer_69(uinput):
	six,nine=True,True
	sum=0
	for i in uinput:
		if i==6:
			six=False
		elif i==9:
			six=True
		elif six and nine:
			sum+=i
		else:
			continue
	return sum

>>> summer_69([1, 3, 5])
9
>>> summer_69([4, 5, 6, 7, 8, 9])
9
>>> summer_69([2, 1, 6, 9, 11])
14
>>> def spy_game(nums):
	for i in range(len(nums)-3):
		if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
			return True
	return False

>>> spy_game([1,2,4,0,0,7,5])
True
>>> spy_game([1,0,2,4,0,5,7])
False
>>> spy_game([1,7,2,0,4,5,0])
False
>>> spy_game([1,7,2,0,4,5,0,0,7])
False
>>> def spy_game(nums):
	for i in range(len(nums)-2):
		if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
			return True
	return False

>>> spy_game([1,7,2,0,4,5,0,0,7])
True
>>> spy_game([1,2,4,0,0,7,5])
True
>>> spy_game([1,0,2,4,0,5,7])
False
>>> def spy_game(nums):
'''This is the real solution for spy_game '''
	for i in range(len(nums)-2):
		if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
			return True
	return False
SyntaxError: expected an indented block
>>> 
>>> def spy_game(nums):
	'''This is the real solution for spy_game '''
	for i in range(len(nums)-2):
		if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
			return True
	return False

>>> spy_game([1,7,2,0,4,5,0,0,7])
True
>>> spy_game([1,2,4,0,0,7,5])
True
>>> spy_game([1,0,2,4,0,5,7])
False
>>> spy_game
<function spy_game at 0x03517420>
>>> help(spy_game)
Help on function spy_game in module __main__:

spy_game(nums)
    This is the real solution for spy_game

>>> COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number¶
SyntaxError: invalid syntax
>>> 
>>> def count_primes(n)
SyntaxError: invalid syntax
>>> def count_primes(n):
	primes=0:
		
SyntaxError: invalid syntax
>>> def count_primes(n):
	primes=0
	for i in range(1,n+1):
		for j in range(1,i-1):
			if i%j==0:
				primes+=1

	
>>> count_primes(100)
>>> def count_primes(n):
	primes=0
	for i in range(1,n+1):
		for j in range(1,i-1):
			if i%j==0:
				primes+=1
	return primes

>>> count_primes(100)
381
>>> def count_primes(n):
	primes=0
	for i in range(1,n+1):
		for j in range(1,i-1):
			if i%j==0:
				primes+=1
				print(i,j)
	return primes

>>> count_primes(9)
3 1
4 1
4 2
5 1
6 1
6 2
6 3
7 1
8 1
8 2
8 4
9 1
9 3
13
>>> def count_primes(n):
	primes=0
	for i in range(2,n+1):
		for j in range(2,i-1):
			if i%j==0:
				primes+=1
				print(i,j)
	return primes

>>> count_primes(100)
4 2
6 2
6 3
8 2
8 4
9 3
10 2
10 5
12 2
12 3
12 4
12 6
14 2
14 7
15 3
15 5
16 2
16 4
16 8
18 2
18 3
18 6
18 9
20 2
20 4
20 5
20 10
21 3
21 7
22 2
22 11
24 2
24 3
24 4
24 6
24 8
24 12
25 5
26 2
26 13
27 3
27 9
28 2
28 4
28 7
28 14
30 2
30 3
30 5
30 6
30 10
30 15
32 2
32 4
32 8
32 16
33 3
33 11
34 2
34 17
35 5
35 7
36 2
36 3
36 4
36 6
36 9
36 12
36 18
38 2
38 19
39 3
39 13
40 2
40 4
40 5
40 8
40 10
40 20
42 2
42 3
42 6
42 7
42 14
42 21
44 2
44 4
44 11
44 22
45 3
45 5
45 9
45 15
46 2
46 23
48 2
48 3
48 4
48 6
48 8
48 12
48 16
48 24
49 7
50 2
50 5
50 10
50 25
51 3
51 17
52 2
52 4
52 13
52 26
54 2
54 3
54 6
54 9
54 18
54 27
55 5
55 11
56 2
56 4
56 7
56 8
56 14
56 28
57 3
57 19
58 2
58 29
60 2
60 3
60 4
60 5
60 6
60 10
60 12
60 15
60 20
60 30
62 2
62 31
63 3
63 7
63 9
63 21
64 2
64 4
64 8
64 16
64 32
65 5
65 13
66 2
66 3
66 6
66 11
66 22
66 33
68 2
68 4
68 17
68 34
69 3
69 23
70 2
70 5
70 7
70 10
70 14
70 35
72 2
72 3
72 4
72 6
72 8
72 9
72 12
72 18
72 24
72 36
74 2
74 37
75 3
75 5
75 15
75 25
76 2
76 4
76 19
76 38
77 7
77 11
78 2
78 3
78 6
78 13
78 26
78 39
80 2
80 4
80 5
80 8
80 10
80 16
80 20
80 40
81 3
81 9
81 27
82 2
82 41
84 2
84 3
84 4
84 6
84 7
84 12
84 14
84 21
84 28
84 42
85 5
85 17
86 2
86 43
87 3
87 29
88 2
88 4
88 8
88 11
88 22
88 44
90 2
90 3
90 5
90 6
90 9
90 10
90 15
90 18
90 30
90 45
91 7
91 13
92 2
92 4
92 23
92 46
93 3
93 31
94 2
94 47
95 5
95 19
96 2
96 3
96 4
96 6
96 8
96 12
96 16
96 24
96 32
96 48
98 2
98 7
98 14
98 49
99 3
99 9
99 11
99 33
100 2
100 4
100 5
100 10
100 20
100 25
100 50
283
>>> def count_primes(n):
	primes=0
	flag=True
	for i in range(1,n+1):
		flag=True
		for j in range(1,i-1):
			if i%j==0:
				flag=False
				break
		if True:
			primes+=1
			
			
	return primes

>>> count_primes(100)
100
>>> def count_primes(n):
	primes=0
	flag=True
	for i in range(1,n+1):
		flag=True
		for j in range(2,i-1):
			if i%j==0:
				flag=False
				break
		if True:
			primes+=1


	return primes

>>> count_primes(100)
100
>>> def count_primes(n):
	primes=0
	flag=True
	for i in range(2,n+1):
		flag=True
		for j in range(2,i-1):
			if i%j==0:
				flag=False
				break
		if True:
			primes+=1


	return primes

>>> count_primes(100)
99
>>> def count_primes(n):
	primes=0
	flag=True
	for i in range(2,n):
		flag=True
		for j in range(2,i-1):
			if i%j==0:
				flag=False
				break
		if True:
			primes+=1


	return primes

>>> count_primes(100)
98
>>> def count_primes(n):
	primes=0
	flag=True
	for i in range(2,n):
		flag=True
		for j in range(2,i-1):
			if i%j==0:
				flag=False
				break
		if True:
			primes+=1
			print(i,j)



	return primes

>>> count_primes(100)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    count_primes(100)
  File "<pyshell#81>", line 12, in count_primes
    print(i,j)
UnboundLocalError: local variable 'j' referenced before assignment
>>> def count_primes(n):
	primes=0
	flag=True
	for i in range(2,n):
		flag=True
		for j in range(2,i-1):
			if i%j==0:
				flag=False
				break
		if True:
			primes+=1
			print(i)



	return primes

>>> count_primes(100)
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
98
>>> def count_primes(n):
	primes=0
	flag=True
	for i in range(2,n+1):
		flag=True
		for j in range(2,i-1):
			if i%j==0:
				flag=False
				break
		if flag:
			primes+=1
			print(i)
	return primes

>>> count_primes(100)
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
25
>>> def count_primes(n):
	primes=0
	flag=True
	for i in range(2,n+1):
		flag=True
		for j in range(2,i-1):
			if i%j==0:
				flag=False
				break
		if flag:
			primes+=1
			print(i)
	return 'prime numbers are : ' + primes

>>> count_primes(100)
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    count_primes(100)
  File "<pyshell#90>", line 13, in count_primes
    return 'prime numbers are : ' + primes
TypeError: can only concatenate str (not "int") to str
>>> def count_primes(n):
	primes=0
	flag=True
	for i in range(2,n+1):
		flag=True
		for j in range(2,i-1):
			if i%j==0:
				flag=False
				break
		if flag:
			primes+=1
			print(i)
	return 'prime numbers are : ' + str(primes)

>>> count_primes(100)
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
'prime numbers are : 25'
>>> 
