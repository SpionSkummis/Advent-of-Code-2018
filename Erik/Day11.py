gridID = 7857
#gridID = 18

def numberExtractor(num,n):
    return (num % 1000)  // 100

#print(numberExtractor(gridID,2))

cellGrid = []
#Create the grid
for x in range(0,300):
    cellGrid.append([])
    for y in range(0,300):
        powerCalc = 0
        powerCalc = ((x + 10) * y + gridID)*(x + 10)
        powerLevel = numberExtractor(powerCalc,2)
        powerLevel -= 5
        cellGrid[x].append(powerLevel)
        

maxSum = 0
maxXpos = 0
maxYpos = 0

for x in range(0,len(cellGrid)-2):
    for y in range(0,len(cellGrid[0])-2):
        tempSum = 0
        for x1 in range(x,x+3):
            for y1 in range(y,y+3):
                tempSum += cellGrid[x1][y1]
        if(tempSum > maxSum):
            maxSum = tempSum
            maxXpos = x
            maxYpos = y

print("Value:", maxSum, "X-pos:", maxXpos, "Y-pos:", maxYpos)

max2sum = 0
max2x = 0
max2y = 0
max2size = 0

for size in range(300,1,-1):
    if(max2sum > ((size*size)*5)):
        break
    for x in range(0,len(cellGrid)-(size-1)):
        for y in range(0,len(cellGrid[0])-(size-1)):
            tempSum = 0
            for x1 in range(x,x+size):
                for y1 in range(y,y+size):
                    tempSum += cellGrid[x1][y1]
            if(tempSum > max2sum):
                max2sum = tempSum
                max2x = x
                max2y = y
                max2size = size
            

print("Value:", max2sum, "X-pos:", max2x, "Y-pos:", max2y,"Gridsize:",max2size)