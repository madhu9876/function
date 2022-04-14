def add():
    list=[50,60,10]
    list1=[10,20,13]
    i=0
    c=[]
    while i<len(list):
        b=list1[i]+list[i]
        c.append(b)
        i=i+1
    print(c)
add()
