#Q6

metRequirement = input("did they meet the requirement: (yes/no) ")
if metRequirement == "yes":
    firmChoice = input("given unconditional offer, is it their firm: (yes/no) ")
    if firmChoice == "yes":
        print("accept admission")
    else:
        rejectedFirm = input("were they rejectde by their firm choice: (yes/no) ")
        if rejectedFirm == "yes":
            print("accept admission")
        else:
            print("closed application")
else:
    mayMeet = input("might they get the requirement: (yes/no) ")
    if mayMeet == "yes":
        firmChoice = input("given conditional offer, is it their firm: (yes/no) ")
        if firmChoice == "yes":
            doesMeet = input("met requirement: (yes/no) ")
            if doesMeet == "yes":
                print("accept admission")
            else:
                print("closed application")
    else:
        rejectedFirm = input("were they rejectde by their firm choice: (yes/no) ")
        if rejectedFirm == "yes":
            doesMeet = input("met requirement: (yes/no) ")
            if doesMeet == "yes":
                print("accept admission")
            else:
                print("closed application")
        else:
            print("closed application")   