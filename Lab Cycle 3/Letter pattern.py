n=int(input("n: "))
if n<=26:
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j),end=" ")
        print()
else:
    print("Invalid input")
