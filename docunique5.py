def fun():
	a=[1,2,3,3,3,3,4,5]
	i=0
	dup=[]
	while i<len(a):
		if a[i] not in dup:
			dup.append(a[i])
		i+=1
	print(dup)
fun()