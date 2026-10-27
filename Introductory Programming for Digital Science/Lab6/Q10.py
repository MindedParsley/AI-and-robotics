email = input("enter an email: ")

for i in range(len(email)):
    if email[i] == "@":
        print(f"the @ was in position {i+1}")