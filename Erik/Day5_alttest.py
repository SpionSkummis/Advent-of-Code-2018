#with open("./inputsE/input05.txt", "rt") as f:
#    inputString = f.read().strip("\n")

def collapsePolymer(collapsedList):
    for i in range((len(collapsedList) -1),1, -1):
        if((ord(collapsedList[i]) == (ord(collapsedList[i-1]) + 32)) or (ord(collapsedList[i]) == (ord(collapsedList[i-1]) - 32))):
            del collapsedList[i-1:i+1]
            i -= 1
    return collapsedList


#Det här ska bli en snabbare grej för att ta bort en viss bokstav. Bakvänd forloop, som ovan? Ta en char eller int som input för vilken bokstav som ska bort, och en lista
#Tänk på att den modifierar listan i nuläget, kan behöva göras bättre!
def removeChar(list):
    a = 0

testString = "dabAcCaCBAcCcaDA"
testList = list(testString)

print(collapsePolymer(testList))

print(testList)