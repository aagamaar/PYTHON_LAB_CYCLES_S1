n=int(input("Enter a three digit number: "))
m=n
s=0
while n!=0:
    x=n%10
    s += x**3
    n//=10
if s == m:
    print("Armstrong number")
else:
    print("Not Armstrong Number")