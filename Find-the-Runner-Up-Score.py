def f():
	num=int(input())
	a=input()
	score=list(map(int,a.split()))
	if num >= 2 and num <= 10 and len(score)>=(-100) and len(score)<=100:
		pass
	else:
		return
	if len(score)>num:
		return
	max=-1000
	for scores in score:
		if scores>max:
			max=scores
	score=list(filter(lambda a:a!=max,score))
	max1=-1000
	for scores in score:
		if scores>max1:
			max1=scores
	return max1

if __name__ == '__main__':
	f()