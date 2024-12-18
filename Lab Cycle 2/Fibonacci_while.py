n=int(input("Enter no. "))
i=0
while i!=n:
    if i==0:
        a1=0
        print(a1,end=" ")
    elif i==1:
        a2=1
        print(a2,end=' ')
    else:
        x=a1+a2
        print(x,end=" ")
        a1,a2=a2,x
    i+=1