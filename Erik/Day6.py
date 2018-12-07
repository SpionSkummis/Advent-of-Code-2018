#Om jag får tid över behöver den här inläsningen ses över, den borde gå att göra mer effektiv eller iallafall snyggare
with open("./inputsE/input06.txt", "rt") as f:
    rawList = f.readlines()
    inputList = []
    for i in range(0,len(rawList)):
        inputList.append(rawList[i].strip("\n").split(", "))
        for i in range(0,len(inputList)):
            inputList[i][0] = int(inputList[i][0])
            inputList[i][1] = int(inputList[i][1])

#Testinput, bra att ha
#inputList = [[1,1],[1,6],[8,3],[3,4],[5,5],[8,9]]

#Funktion för att grovanalysera input. Behövs egentligen inte
def findEdges(list):
    minX = 1000
    minY = 1000
    maxX = 0
    maxY = 0
    for i in range(0,len(inputList)):
        if(list[i][0] < minX):
            minX = list[i][0]
        if(list[i][1] < minY):
            minY = list[i][1]
        if(list[i][0] > maxX):
            maxX = list[i][0]
        if(list[i][1] > maxY):
            maxY = list[i][1]
    print(minX,minY,maxX,maxY)


def arrayCreator(lenX,lenY):
    mainArray = []
    for x in range(0,lenX):
        mainArray.append([])
        for y in range(0,lenY):
            mainArray[x].append(0)
    return mainArray.copy()

def distanceCalc(listA, listB):
    return (abs(listA[0]-listB[0]) + abs(listA[1]-listB[1]))

def multiDistanceCalc(xyList, bigList):
    distanceSum = 0
    for i in range(0,len(bigList)):
        distanceSum += distanceCalc(xyList,bigList[i])
    return distanceSum

#Del ett, inte speciellt snabb. Skapar ett rutnät, sätter varje ruta till en hänvisning till vilken listplats den närmsta koordinaten har
grid = arrayCreator(400,400)
for i in range(0,len(grid)):
    for n in range(0,len(grid[0])):
        closeCoord = 0
        closeRange = 9999
        secondRange = 0
        secondCoord = 9999
        dist = 0
        for a in range(0,len(inputList)):
            dist = distanceCalc([i,n],inputList[a])
            if(dist <= closeRange):
                secondCoord = closeCoord
                secondRange = closeRange
                closeRange = dist
                closeCoord = a
        if(closeRange == secondRange):
            grid[i][n] = -1
        else:
            grid[i][n] = closeCoord

#Rör den kanten är den oändlig. Vilka rör kanten?
nextToEdge = []
for i in range(0,len(grid)):
    for n in range(0,len(grid[0])):
        if( ((i==0) or (i==(len(grid)-1))  or (n==0) or  (n==(len(grid[i])-1))) and (grid[i][n] not in nextToEdge)):
            nextToEdge.append(grid[i][n])

#Skriv över alla oändliga områden
for i in range(0,len(grid)):
    for n in range(0,len(grid[0])):
        if(int(grid[i][n]) in nextToEdge):
            grid[i][n] = -1

#Vilken siffra finns flest gånger i koordinatsystemet? Antalet gånger den förekommer är största området. Hitta och skriv ut!
ownedSquares = [0]*len(inputList)
for i in range(0,len(grid)):
    for n in range(0,len(grid[0])):
        if(grid[i][n] >= 0):
            ownedSquares[(grid[i][n])] += 1

print("Part 1: " +str(max(ownedSquares)))



#Del 2. Gör ett nytt fint rutnät. Sätt varje ruta till avståndet den har till samtliga koordinater.
distanceGrid = arrayCreator(400,400)
for i in range(0,len(distanceGrid)):
    for n in range(0,len(distanceGrid[0])):
        distanceGrid[i][n] = multiDistanceCalc([i,n],inputList)

#Summera antalet rutor som ligger nära nog. Printa som svaret.
areaSize = 0
for i in range(0,len(distanceGrid)):
    for n in range(0,len(distanceGrid[0])):
        if(distanceGrid[i][n] < 10000):
            areaSize += 1

print("Part 2: " +str(areaSize))
