num=[50,40,23,70,56,12,5,10,7]
i=0
max=0
while i<len(num):
	if num[i]>max:
		max=num[i]
	i=i+2
print('sec',max)