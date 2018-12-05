with open("./inputsE/input05.txt", "rt") as f:
    inputList = list(f.read().strip("\n"))

#testString = "dabAcCaCBAcCcaDA"

def collapsePolymer(inList):
    collapsedList = inList
    for i in range((len(collapsedList) -1),0, -1):
        if((ord(collapsedList[i]) == (ord(collapsedList[i-1]) + 32)) or (ord(collapsedList[i]) == (ord(collapsedList[i-1]) - 32))):
            del collapsedList[i-1:i+1]
            i -= 1
    return collapsedList

def removeChar(inList, charInt):
    purgeList = inList # Bättre att göra nytt än att ändra i det som finns?
    smallChar = chr(charInt+97)
    bigChar = chr(charInt+65)
    for i in range((len(purgeList) -1),-1, -1):
        if((purgeList[i] == smallChar) or (purgeList[i] == bigChar)):
            del purgeList[i]
    return purgeList

print(len(collapsePolymer(inputList)))

lenAfterPurge = [0]*26


for i in range(0, len(lenAfterPurge)):
    lenAfterPurge[i] = len(collapsePolymer(removeChar(inputList.copy(),i)))

print(min(lenAfterPurge))