def fun():
		a=int(input("num"))
		i=1
		c=0
		while i<=a:
			if a%i==0:
				c=c+1
			i=i+1
		if c==2:
			print('prime no',a)
		else:
			print('not prime no',a)
fun()