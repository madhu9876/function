def fun():
    a=[5,10,50,20]
    b=[2,20,3,5]
    i=0
    c=[]
    while i<len(a):
        d=a[i]*b[i]
        c.append(d)
        i=i+1
    print(c)
fun()