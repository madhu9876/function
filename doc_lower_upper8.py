def fun():
	str='The quick BrowFox'
	i=0
	c=1
	c1=-3
	while i<len(str):
		if str[i]==" ":
			c=c+1
		else:
			c1=c1+1
		i=i+1
	print("No of uppercase:",c)
	print("No of lowercase:",c1)
fun()