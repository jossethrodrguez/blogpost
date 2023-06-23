user_number = int(input("Type a number, and I tell you if is a ten multiple: "))

if user_number % 10 == 0:
    print(f"\n{user_number} is a ten multiple")
else:
    print(f"\n{user_number} is not a ten multiple")
