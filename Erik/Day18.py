
#with open("./inputsE/input18.txt", "rt") as f:
with open("./inputsE/input18-t.txt", "rt") as f:
    rawInput = f.read().splitlines()
xLen = len(rawInput[0])
yLen = len(rawInput)

grid = []
grid.append(["k"]*(xLen+2))
for y in range(0,yLen):
    row = ["k"]
    for x in range(0,xLen):
        row.append(rawInput[y][x])
    row.append("k")
    grid.append(row.copy())
grid.append(["k"]*(xLen+2))

def findAdj(inList, ypos, xpos):
    adjTree = 0
    adjYard = 0
    for y in range(ypos-1,ypos+2):
        for x in range(xpos-1, xpos+2):
            if(inList[y][x] == "|"):
                adjTree += 1
            elif(inList[y][x] == "#"):
                adjYard += 1
    if(inList[ypos][xpos] == "|"):
        adjTree -= 1
    elif(inList[ypos][xpos] == "#"):
        adjYard -= 1
    return adjTree, adjYard

def getNextSquare(inList, ypos, xpos):
    currSq = inList[ypos][xpos]
    if(currSq == "."):
        if(findAdj(inList,ypos,xpos)[0] > 2):
            return "|"
        else:
            return "."
    if(currSq == "|"):
        if(findAdj(inList,ypos,xpos)[1] > 2):
            return "#"
        else:
            return "|"
    if(currSq == "#"):
        if((findAdj(inList,ypos,xpos)[0] > 0) and (findAdj(inList,ypos,xpos)[1] > 0)):
            return "#"
        else:
            return "."
    print("do not reach")

emptyGrid = [["k"]*(xLen+2)]*(yLen+2)
currentGen = grid.copy()
nextGen = emptyGrid.copy()
generations =1
print(len(grid),len(grid[0]),len(grid[1]))
[print(x) for x in currentGen]
print("\n")

for i in range(0,generations):
    for y in range(1,yLen+1):
        for x in range(1,xLen+1):
            nextGen[y][x] = getNextSquare(currentGen,y,x)
    currentGen = nextGen.copy()

#print(currentGen)
treeCount = 0
yardCount = 0
ktestCount = 0
for y in range(0,len(currentGen)):
    nextGen = emptyGrid.copy()
    for x in range(0,len(currentGen[0])):
        if(currentGen[y][x] == "#"):
            yardCount += 1
        elif(currentGen[y][x] == "|"):
            treeCount += 1
        elif(currentGen[y][x] == "k"):
            ktestCount += 1

for row in range(0,len(currentGen)):
    print(currentGen[row])

print(treeCount,yardCount,ktestCount,(treeCount*yardCount))


#436305 är fel, för lågt



#1711 255 154 436305