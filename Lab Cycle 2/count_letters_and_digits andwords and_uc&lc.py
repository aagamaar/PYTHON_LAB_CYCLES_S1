n=input("Enter the string: ")
m=n.strip()
l=d=w=uc=lc=0
for i in m:
    if i.isalpha():
        l+=1
        if i.isupper():
            uc+=1
        else:
            lc+=1
    else:
        if i.isdigit():
            d+=1
f=m.split()
print("Letters:",l)
print("Digits:",d)
print("Uppercase:",uc)
print("Lowercase:",lc)
print("Words:",len(f))


