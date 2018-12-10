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
    
#Till del 2:
p2letterDict = letterDict.copy()
p2allLetters = allLetters.copy()


#Kollar vilka bokstäver som kan köras genom att ta de som är upplåsta (inga krav för att köra)
#och de som blir upplåsta (alla spärrbokstäver i listan över körda bokstäver)
def findUnblocked(mainDict, orderList):
    resultList = []
    for key in mainDict:
        if(all(elem in orderList for elem in mainDict[key])):
            resultList.append(key)
    removeList = []
    for i in range(0,len(resultList)):
        if(resultList[i] in orderList):
            removeList.append(resultList[i])
    for i in range(0,len(removeList)):
        resultList.remove(removeList[i])
    resultList.sort()
    return resultList


while(len(finalOrder) < len(allLetters)):
    canBeRun = findUnblocked(letterDict,finalOrder)
    canBeRun.sort()
    finalOrder.append(canBeRun[0])

print(finalOrder)
print("Ans 1: " +"".join(finalOrder))






def p2findUnblocked(mainDict, orderList, startedList):
    resultList = []
    removeSet = set()
    for key in mainDict:
        if(all(elem in orderList for elem in mainDict[key])):
            resultList.append(key)

    for i in range(0,len(resultList)):
        if(resultList[i] in orderList):
            removeSet.add(resultList[i])
    for i in range(0,len(resultList)):
        if(resultList[i] in startedList):
            removeSet.add(resultList[i])

    for elem in removeSet:
        resultList.remove(elem)

    resultList.sort()
    return resultList


def findStepTime(oneCharString):
    return (ord(oneCharString)-4)

class SleighBuilder:
    def __init__(self):
        self.currentTime = 0
        self.timeWhenDone = 0
        self.workingLetter = ""

    def getState(self,time):
        self.currentTime = time
        if((self.workingLetter == "")):
            return "Waiting"
        elif(self.timeWhenDone == self.currentTime):
            return "Done"
        elif(self.timeWhenDone < self.currentTime):
            return "Working"
        else:
            #print("Error in getState function")
            return "Error"
    
    def passDoneLetter(self):
        self.tempLetter = self.workingLetter
        self.workingLetter = ""
        return self.tempLetter

    def startNewLetter(self, charStr):
        self.workingLetter = charStr
        self.timeWhenDone = self.currentTime + ord(self.workingLetter) -4




p2finalOrder = []
p2startedLetters = []

worker1 = SleighBuilder()
worker2 = SleighBuilder()
worker3 = SleighBuilder()
worker4 = SleighBuilder()
worker5 = SleighBuilder()

a = 0
while(len(p2finalOrder) < len(p2allLetters)):
    if(worker1.getState(a) == "Done"):
        p2finalOrder.append(worker1.passDoneLetter())
    if(worker2.getState(a) == "Done"):
        p2finalOrder.append(worker2.passDoneLetter())
    if(worker3.getState(a) == "Done"):
        p2finalOrder.append(worker3.passDoneLetter())
    if(worker4.getState(a) == "Done"):
        p2finalOrder.append(worker4.passDoneLetter())
    if(worker5.getState(a) == "Done"):
        p2finalOrder.append(worker5.passDoneLetter())

    canBeRun = p2findUnblocked(p2letterDict,p2finalOrder,p2startedLetters)
    if(worker1.getState(a) == "Waiting" and len(canBeRun) > 0):
        p2startedLetters.append(canBeRun[0])
        worker1.startNewLetter(canBeRun.pop(0))

    canBeRun = p2findUnblocked(p2letterDict,p2finalOrder,p2startedLetters)
    if(worker2.getState(a) == "Waiting" and len(canBeRun) > 0):
        p2startedLetters.append(canBeRun[0])
        worker2.startNewLetter(canBeRun.pop(0))
        
    canBeRun = p2findUnblocked(p2letterDict,p2finalOrder,p2startedLetters)
    if(worker3.getState(a) == "Waiting" and len(canBeRun) > 0):
        p2startedLetters.append(canBeRun[0])
        worker3.startNewLetter(canBeRun.pop(0))

    canBeRun = p2findUnblocked(p2letterDict,p2finalOrder,p2startedLetters)
    if(worker4.getState(a) == "Waiting" and len(canBeRun) > 0):
        p2startedLetters.append(canBeRun[0])
        worker4.startNewLetter(canBeRun.pop(0))

    canBeRun = p2findUnblocked(p2letterDict,p2finalOrder,p2startedLetters)
    if(worker5.getState(a) == "Waiting" and len(canBeRun) > 0):
        p2startedLetters.append(canBeRun[0])
        worker5.startNewLetter(canBeRun.pop(0))

    a += 1

print(p2finalOrder)
print("".join(p2finalOrder))
print("Ans2: ", (a-1))
