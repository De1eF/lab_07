def getLongestStringLength(stringList):
    longestLength = 0
    
    for i in range(0, len(stringList)):
        if len(stringList[i]) > longestLength:
            longestLength = len(stringList[i])
    
    return longestLength

def equalizeStringWithStar(str, upToLength):
    resultString = str
    while len(resultString) < upToLength:
        resultString = resultString + "*"
    
    return resultString

def equalizeStringListWithStar(stringList):
    longestLength = getLongestStringLength(stringList)
    resultList = list()
    
    for i in range(0, len(stringList)):
        resultList.append(equalizeStringWithStar(stringList[i], longestLength))
        
    return resultList

#Task

stringCount = int(input("Enter string amount (int): "))

stringList = list()

while stringCount > 0:
    stringList.append(input("Enter a string value (str): "))
    stringCount -= 1
    
print("\n Equalized string list:")

for s in equalizeStringListWithStar(stringList):
    print(s)
