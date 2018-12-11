import threading
gridID = 7857
#gridID = 18

def numberExtractor(num,n):
    return (num % 1000)  // 100

cellGrid = []
for x in range(0,300):
    cellGrid.append([])
    for y in range(0,300):
        powerCalc = 0
        powerCalc = ((x + 10) * y + gridID)*(x + 10)
        powerLevel = numberExtractor(powerCalc,2)
        powerLevel -= 5
        cellGrid[x].append(powerLevel)

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, grid, offset):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.grid = grid
      self.offset = offset
   def run(self):
      print("Starting " + self.name)
      search_grid(self.grid, self.offset)
      print("Exiting " + self.name)

    def search_grid(threadName, grid, offset):
        max2sum = 0
        max2x = 0
        max2y = 0
        max2size = 0
        for size in range(offset,300,4):
            for x in range(0,len(grid)-(size-1)):
                for y in range(0,len(grid[0])-(size-1)):
                    tempSum = 0
                    for x1 in range(x,x+size):
                        for y1 in range(y,y+size):
                            tempSum += cellGrid[x1][y1]
                    if(tempSum > max2sum1):
                        max2sum = tempSum
                        max2x = x
                        max2y = y
                        max2size = size
        print("Value1:", max2sum, "X-pos:", max2x, "Y-pos:", max2y,"Gridsize:",max2size)
        return ("Value1: "+str(max2sum)+" X-pos: "+str(max2x)+" Y-pos: "+str(max2y)+" Gridsize: "+str(max2size))



# Create new threads
thread1 = myThread(1, "Thread-1", cellGrid, 1)
thread1 = myThread(2, "Thread-2", cellGrid, 2)
thread1 = myThread(3, "Thread-3", cellGrid, 3)
thread1 = myThread(4, "Thread-4", cellGrid, 4)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()

print("Exiting Main Thread")