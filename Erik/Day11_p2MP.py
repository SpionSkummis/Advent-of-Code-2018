import multiprocessing

def numberExtractor(num,n):
    return (num % 1000)  // 100

def worker(num):
    print("Starting worker",num)
    gridID = 7857
    cellGrid = []
    for x in range(0,300):
        cellGrid.append([])
        for y in range(0,300):
            powerCalc = 0
            powerCalc = ((x + 10) * y + gridID)*(x + 10)
            powerLevel = numberExtractor(powerCalc,2)
            powerLevel -= 5
            cellGrid[x].append(powerLevel)
    
    max2sum = 0
    max2x = 0
    max2y = 0
    max2size = 0
    for size in range(num,300,4):
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
                
    print("Worker",num,"Value1:", max2sum, "X-pos:", max2x, "Y-pos:", max2y,"Gridsize:",max2size)
    return ("Value: "+str(max2sum)+" X-pos: "+str(max2x)+" Y-pos: "+str(max2y)+" Gridsize: "+str(max2size))




if __name__ == '__main__':
    jobs = []
    for i in range(1,5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()