def add(a,b):
    if b==0:
        return a
    else:
        return add(a+1,b-1)
a=int(input("Enter the 1st num: "))
b=int(input("Enter the 2nd num: "))
print("Here, is the Sum: ",add(a,b))