n=int(input("Enter a number: "))
sum = 0
while n!=0:
    x = n%10
    sum+=x
    n//=10
print("Sum of digits in the number: ", sum)
