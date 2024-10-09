import random

def generateString(length):
    result = ""
    
    while len(result) < length:
        result += chr(random.randint(97, 122))
    
    return result

def generateStringList(stringCount):
    resultList = list()
    strCnt = int(stringCount)
    
    while len(resultList) < strCnt:
        resultList.append(generateString(strCnt))
        
    return resultList

def countSymbolsInString(string, symbol):
    count = 0
    
    for c in string:
        if c == symbol:
            count += 1
    
    return count

def findStringWithLargestAmountOfSymbols(stringList, symbol):
    largestAmountOfSymbols = 0
    stringWithLargestAmountOfSymbols = ""
    
    for s in stringList:
        amountOfSymbols = countSymbolsInString(s, symbol)
        if (largestAmountOfSymbols < amountOfSymbols):
            largestAmountOfSymbols = amountOfSymbols
            stringWithLargestAmountOfSymbols = s
            
    return stringWithLargestAmountOfSymbols

#Task
n = input("N: ")
generatedStringList = generateStringList(n)

print("Generated strings:")
for s in generateStringList(n):
    print(s)
    
print("\n Largest amount of 'o' is in: \n", findStringWithLargestAmountOfSymbols(generatedStringList, "o"))
