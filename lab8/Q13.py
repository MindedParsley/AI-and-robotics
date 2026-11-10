str1 = set(list(input("enter the first string: ")))
str2 = set(list(input("enter teh second string: ")))


print(f"left over characters: {sorted((str2 - str1) | (str1 - str2))}")