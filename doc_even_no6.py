def fun(a):
	i=1
	even=[]
	while i<len(a):
		if i%2==0:
			even.append(i)
		i+=1
	print(even,end=" ")
fun([1,2,3,4,5,6,7,8,9])