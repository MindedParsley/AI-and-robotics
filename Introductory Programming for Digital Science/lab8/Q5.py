inString = input("enter a string to reverse: ")

#iterative inverse
def reverse_i(inString):
    outString = ""

    for i in range(len(inString)-1,-1,-1):
        outString += inString[i]
    
    return outString

#recursive inverse
def reverse_r(inString):
    if len(inString) <= 1:
        return inString

    return reverse_r(inString[1:]) + inString[0]

print(f"iterive: {reverse_i(inString)}")
print(f"recursive: {reverse_r(inString)}")