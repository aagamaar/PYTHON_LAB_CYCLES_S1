def mult(a,b):
    if b==0:
        return 0
    else:
        return a + mult(a,b-1)
a=int(input("Enter  1st num: "))
b=int(input("Enter  2nd num: "))
print("Product: ",mult(a,b))