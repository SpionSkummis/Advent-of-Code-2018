import re

with open("./inputsE/input07.txt", "rt") as f:
    rawInput = f.read().splitlines()

#print(rawInput)

finalOrder = []
inputList = []
leftCol = set()#[]
rightCol = set()#[]
for i in range(0,len(rawInput)):
    tempList = ["",""]
    tempList[0] = re.search(" ([A-Z]) .+ ([A-Z]) ", rawInput[i]).group(1)
    tempList[1] = re.search(" ([A-Z]) .+ ([A-Z]) ", rawInput[i]).group(2)
    leftCol.add(tempList[0])#ppend(tempList[0])
    rightCol.add(tempList[1])#ppend(tempList[1])
    inputList.append(tempList)


allLetters = set()
for i in range(0,len(inputList)):
    allLetters.add(inputList[i][0])
    allLetters.add(inputList[i][1])

lettersReq = {}
smallReq = []
for char in allLetters:
    lettersReq[char] = ""
for i in range(0,len(inputList)):
    lettersReq[inputList[i][1]] = lettersReq[inputList[i][1]] +str(inputList[i][0])

canRun = []
for key in lettersReq:
    if(lettersReq[key] == ""):
        canRun.append(key)
canRun.sort()
finalOrder.append(canRun[0])
for key in lettersReq:
    lettersReq[key].replace(str(canRun[0]), "")



print(lettersReq)
print(canRun)
"""
#leftCol.sort()
#rightCol.sort()

#print(leftCol)
#print(rightCol)
canBegin = []
hasBegun = []
for x in leftCol:
    if(x not in rightCol):
        canBegin.append(x)
        #print(x)


canBegin.sort()
print(canBegin)
justRun = canBegin[0]
hasBegun.append(canBegin.pop(0))

for i in range(0,len(inputList)):
    if((inputList[i][0]) == justRun) and (inputList[i][1] not in canBegin):
        canBegin.append(inputList[i][1])
        #print(inputList[i][1])
canBegin.sort()
print(canBegin)
"""