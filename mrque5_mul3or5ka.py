def fun():
    i=0
    s=0
    while i<=10:
        if i%3==0 or i%5==0: #or ka use hoga 
            s=s+i
        i=i+1
    print(s)
fun()        