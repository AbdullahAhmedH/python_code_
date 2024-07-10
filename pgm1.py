a = int(input("Enter hour:\n"))

if a == 0 or a == 24:
    print("12 AM")
elif a<12:
    print(a,"AM")
elif a == 12:
    print("12 PM")
elif a>12:
    print(a-12,"PM")
