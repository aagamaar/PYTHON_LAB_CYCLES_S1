import math
n=input("Enter the number: ")
s=0
for i in n:
    s += math.factorial(int(i)) 
if s==int(n):
    print(n," is a Krishnamurthy number. ")
else:
    print(n," is not a Krishnamurthy number. ")




