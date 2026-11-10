str1 = set(list(input("enter the first string: ")))
str2 = set(list(input("enter teh second string: ")))
alphabetSet = set(list('abcdefghijklmnopqrstuvwxyz'))

print(f"left over characters: {sorted(alphabetSet - (str1 | str2))}")