startDict = {1:'A', 2:'B', 3:'C', 4:'D'}
invertDict = {}
for i in startDict.keys():
    invertDict[startDict[i]] = i

print(invertDict)