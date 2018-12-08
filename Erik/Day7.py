#Läs in rubbet, gärna som tre olika listor och ett set med alla bokstäver
#Gör ett dictionary med alla bokstäver, som värde skall de ha en sträng med alla bokstäver som måste klaras av först??
#Om bokstaven har tomt värde och inte finns i listan "körda bokstäver" kan den köras
#Kör, lägg till, rotera?


#Läs in första filen
import re
with open("./inputsE/input07.txt", "rt") as f:
    rawInput = f.read().splitlines()
#Testinput vid behov:
#rawInput = ["Step C must be finished before step A can begin.","Step C must be finished before step F can begin.","Step A must be finished before step B can begin.","Step A must be finished before step D can begin.","Step B must be finished before step E can begin.","Step D must be finished before step E can begin.","Step F must be finished before step E can begin."]

#Formatterar input till något eventuellt användbart
finalOrder = [] #Listan med alla bokstäver som körts och deras ordning.
allLetters = set() #Set med alla bokstäver som förekommer
mainList = [] #Listan enligt [väkol,hökol]
leftCol = [] #Alla bokstäver i vänsterkolumnen i ordning, typ
rightCol = [] #Alla bokstäver i högerkolumnen i ordning, typ
for i in range(0,len(rawInput)):
    tempList = ["",""]
    tempList[0] = re.search(" ([A-Z]) .+ ([A-Z]) ", rawInput[i]).group(1)
    tempList[1] = re.search(" ([A-Z]) .+ ([A-Z]) ", rawInput[i]).group(2)
    allLetters.add(tempList[0])
    allLetters.add(tempList[1])
    leftCol.append(tempList[0])
    rightCol.append(tempList[1])
    mainList.append(tempList.copy())

#Deklarera ett dictionary med alla tillgängliga bokstäver:
letterDict = {}
for key in allLetters:
    letterDict[key] = []

#Hitta vilka bokstäver som måste vara klara för att köra nästa
#Titta i högerkolumnen, mainList[left,right], för dict[key=right], value += left
for i in range(0,len(mainList)):
    if(mainList[i][0] not in letterDict[mainList[i][1]]):
        letterDict[mainList[i][1]].append(mainList[i][0])
    

#Kollar vilka bokstäver som kan köras genom att ta de som är upplåsta (inga krav för att köra)
#och de som blir upplåsta (alla spärrbokstäver i listan över körda bokstäver)
def findUnblocked(mainDict, orderList):
    resultList = []
    for key in mainDict:
        if(all(elem in orderList for elem in mainDict[key])):
            resultList.append(key)
            print(key)
    removeList = []
    for i in range(0,len(resultList)):
        if(resultList[i] in orderList):
            removeList.append(resultList[i])
    for i in range(0,len(removeList)):
        resultList.remove(removeList[i])
    return resultList


while(len(finalOrder) < len(allLetters)):
    canBeRun = findUnblocked(letterDict,finalOrder)
    canBeRun.sort()
    finalOrder.append(canBeRun[0])

print(finalOrder)
print("".join(finalOrder))