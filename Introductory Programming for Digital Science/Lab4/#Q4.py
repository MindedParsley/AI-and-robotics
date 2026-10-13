#Q4

temp = int(input("enter the temp: "))
humid = int(input("enter the humidity: "))

if temp >= 25 and humidity > 60:
    print("muggy day today")
elif temp >= 25:
    print("warm, but not muggy today")
elif temp >= 18:
    print("pleasant today")
elif temp >= 10:
    print("cold today")
else:
    print("cool today")