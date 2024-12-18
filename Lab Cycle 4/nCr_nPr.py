def fact(n):
    if n==0:
        return 1
    else:
        return n* fact(n-1)
n=int(input("Enter  n: "))
r=int(input("Enter  r: "))
n_fact=fact(n)
r_fact=fact(r)
nr_fact=fact(n-r)
nCr=n_fact/(r_fact*nr_fact)
nPr=n_fact/nr_fact
print("nCr: ",nCr)
print("nPr: ",nPr)

