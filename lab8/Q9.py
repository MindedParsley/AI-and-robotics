inputString = input("enter a string: ")

vowels = sum(1 for c in inputString if c.isalpha() and c.lower() in "aeiou")
print(f"there were {vowels} vowels in the string")