nums = [12, 56, 72, 33, 1, 7,]

outputStr = ""
for i in range(len(nums)):
    outputStr += str(nums[len(nums)-(i+1)])
print(f"list backwards is {outputStr}")

outputStr = ""
for i in range(len(nums)):
    if i%2 == 0:
        outputStr += nums[i]
print(f"all even index's are {outputStr}")