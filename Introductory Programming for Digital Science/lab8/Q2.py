password_lookup = {}

while True:
    user = input("enter your username: ")
    if user == "z":
        break
    elif user not in password_lookup.keys():
        password = input("create your password: ")
        password_lookup[user] = password
    else:
        password = input("enter your password: ")
        if password != password_lookup[user]:
            print("incorrect password")
        else:
            print("welcome")
            break 