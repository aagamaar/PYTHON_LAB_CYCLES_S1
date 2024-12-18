def reverse(s):
    if len(s)==0 or len(s)==1:
        return s
    else:
        return reverse(s[1:])+s[0]
s=input("Enter a string: ")
print(reverse(s))