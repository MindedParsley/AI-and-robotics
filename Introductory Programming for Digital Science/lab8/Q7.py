inputStr = input("enter a string: ")
freq = {}
for i in range(len(inputStr)):
    if inputStr[i] not in freq:
        freq[inputStr[i]] = 1
    else: 
        freq[inputStr[i]] += 1

print(freq)

