#pay and return ------------------------------------------

acceptedCoin = ["£20","£10","£5","£2","£1","50p","20p","10p","5p","2p","1p"]
acceptedCoinValues = [20,10,5,2,1,.5,.2,.1,.05,.02,.01]
inputtedCoinTotal = 0

maxPrice = 5.67
minPrice = 0.09

#inputting the price of the item till its between the max and min value
priceOfItem = float(input("enter the price of the purchase: "))
while priceOfItem < minPrice or priceOfItem > maxPrice:
    print("the price ranges from £0.09 - £5.67")
    priceOfItem = float(input("enter the price of the purchase: "))

#looping thought the coin values till the user has inputed a total valu egreater ot equal to the items price
for i in range(len(acceptedCoin)):
    coinIn = int(input(f"how many {acceptedCoin[i]} paid in: "))
    while coinIn < 0:
        print("enter a value greater than -1")
        coinIn = int(input(f"how many {acceptedCoin[i]} paid in: "))
    inputtedCoinTotal += (acceptedCoinValues[i] * coinIn)
    if priceOfItem <= inputtedCoinTotal:
        break

#looping through the coin values to get the biggest amount of each coin to return
priceBack = inputtedCoinTotal - priceOfItem
print(f"the change £{priceBack} will be paid with: ")
for i in range(len(acceptedCoinValues)):
    if acceptedCoinValues[i] <= priceBack:
        print(f"{acceptedCoin[i]} x {priceBack//acceptedCoinValues[i]}")
        priceBack -= acceptedCoinValues[i] * (priceBack//acceptedCoinValues[i])

print("thank you")
#-----------------------------------------------
