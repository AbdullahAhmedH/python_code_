a = input("Enter string:")
b = ""
for i in range(len(a)-1,-1,-1):
    b+=a[i]

print("Reverse =", b)
