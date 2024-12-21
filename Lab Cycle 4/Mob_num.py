def isMobileNumber(n):
    if len(n) != 10:
        return False
    if n[0] not in "789":
        return False
    if not n.isdigit():
        return False
    return True

n = input("Enter your mobile number: ")
result = isMobileNumber(n)
print("This is a valid mobile number" if result else "This is an invalid mobile number")