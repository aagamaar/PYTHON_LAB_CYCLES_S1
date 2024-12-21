def mult(a,b):
    if b==0:
        return 0
    else:
        return a + mult(a,b-1)
a=int(input("Enter the 1st num: "))
b=int(input("Enter the 2nd num: "))
print("Here, is the Product: ",mult(a,b))