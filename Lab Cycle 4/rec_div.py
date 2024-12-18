def div(a,b):
    if b==0:
        return a
    else:
        return div(b,a%b)
a=int(input("1st num: "))
b=int(input("2nd num: "))
if a>=0 and b>=0:
    print("Greatest Common Divisor", div(a,b))
else:
    print("Error")