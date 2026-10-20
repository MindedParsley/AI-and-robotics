string = input("enter your string: ")
vowels = ["a","e","i","o","u"]
consonants = [char for char in string if char.isalpha() and char.lower() not in vowels]

print(consonants)

divisible3 = []
for i in range(1,100+1):
    if i%3 == 0:
        divisible3.append(i)
print(f"the numbers that are divisible by 3 are {divisible3}")

tempC = [1,2,3,4,5,6]
tempF = [(temp*2+30) for temp in tempC]
print(tempF)