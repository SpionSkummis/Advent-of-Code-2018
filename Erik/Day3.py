import re, numpy

instructionsList = []
with open("./inputsE/input03.txt", "rt") as f:
    instructionsList = f.read().splitlines()

def formatInstructions(listIn):
    finalList = []
    for i in range(0,len(listIn)):
        tempList = [0]*4
        regRead = re.search("@ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)", listIn[i])
        for j in range(0,4):
            tempList[j] = int(regRead.group(j+1))
        finalList.append(tempList)
    return finalList


shortInst = formatInstructions(instructionsList)

fabricSheet = numpy.zeros((1000,1000),dtype=int)
for i in range(0,len(shortInst)):
    startX = shortInst[i][0]
    startY = shortInst[i][1]
    repX = shortInst[i][2]
    repY = shortInst[i][3]
    for x in range(startX,startX+repX):
        for y in range(startY,startY+repY):
            fabricSheet[x][y] += 1

multiCutSquares = 0
for x in range(0,len(fabricSheet)):
    for y in range(0,len(fabricSheet[0])):
        if(fabricSheet[x][y] > 1):
            multiCutSquares += 1

print(multiCutSquares)

for i in range(0,len(shortInst)):
    startX = shortInst[i][0]
    startY = shortInst[i][1]
    repX = shortInst[i][2]
    repY = shortInst[i][3]
    testCounter = 0
    for x in range(startX,startX+repX):
        for y in range(startY,startY+repY):
            testCounter += fabricSheet[x][y]
    if(testCounter == (repX*repY)):
        print("Found! At: " +str(i + 1)) #Listan ej nollindexerad
