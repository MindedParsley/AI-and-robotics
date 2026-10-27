ss_num = "123-456-789"

NotNumeric = False
for i in range(len(ss_num)):
    if not ss_num[i].isnumeric():
        NotNumeric = True
        break

print(NotNumeric)