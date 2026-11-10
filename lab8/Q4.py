Name = input("enter your name: ")
cons = sum(1 for c in Name if c.isalpha() and c.lower() not in "aeiou")
vowels = len(Name) - cons

print(f"constonants: {cons}, vowels: {vowels}")