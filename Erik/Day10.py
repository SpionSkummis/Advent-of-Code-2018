import re
import tkinter as tk

def getInput(mainOrTest):
    returnList = []
    filePath = "./inputsE/input10.txt"
    if(mainOrTest == "test"):
        filePath = "./inputsE/Outputs/test10.txt"
    with open(filePath,"rt") as f:
        rawInput = f.read().splitlines()

    for i in range(0,len(rawInput)):
        starInfo = [0,0,0,0] #xpos, ypos, xdelta, ydelta
        regSearch = re.search("< ?(-?[0-9]+), *(-?[0-9]+)>.+< *(-?[0-9]+), *(-?[0-9]+)",rawInput[i])
        for j in range(0,4):
            starInfo[j] = int(regSearch.group(j+1))
        returnList.append(starInfo)

    return returnList

def makeGrid(inputList, repeats):
    newGrid = []
    for i in range(0,len(inputList)):
        starPos = [0,0]
        starPos[0] = inputList[i][0] + (inputList[i][2]*repeats)
        starPos[1] = inputList[i][1] + (inputList[i][3]*repeats)
        newGrid.append(starPos)
    return newGrid.copy()

def findGridLimits(inGrid):
    extremes = [99999,-99999,99999,-99999] #xmin, xmax, ymin, ymax
    for i in range(0,len(inGrid)):
        if(inGrid[i][0] > extremes[1]):
            extremes[1] = inGrid[i][0]
        if(inGrid[i][0] < extremes[0]):
            extremes[0] = inGrid[i][0]

        if(inGrid[i][1] > extremes[3]):
            extremes[3] = inGrid[i][1]
        if(inGrid[i][1] < extremes[2]):
            extremes[2] = inGrid[i][1]
        
    return extremes

def findSmallGrid(inList):
    arbReps = 20000
    smallrep = 0
    size = 9999999999999999999999999
    for i in range(0,arbReps):
        testGrid = makeGrid(inList,i)
        if((findHeight(testGrid) + findWidh(testGrid)) < size):
            size = (findHeight(testGrid) + findWidh(testGrid))
            smallrep = i
    return smallrep




def findHeight(inGrid):
    gridExr = findGridLimits(inGrid)
    return gridExr[1]-gridExr[0]

def findWidh(inGrid):
    gridExr = findGridLimits(inGrid)
    return gridExr[3]-gridExr[2]

def findNiceRepeats(inputList): #Om man vill. Tanken är att den hittar raka linjer
    arbReps = 25000
    for i in range(0,arbReps):
        testGrid = makeGrid(inputList,i)
        for j in range(0,len(testGrid)):
            pass

mainInput = getInput("main")

gridNrToAnalyze = findSmallGrid(mainInput)
#gridNrToAnalyze = 10639 #Tillfälligt hårdkodat så att det ska gå snabbare
print("Antalet sekunder innan meddelandet dyker upp: ",gridNrToAnalyze)

analyzeGrid = makeGrid(mainInput,gridNrToAnalyze)
print("Ungefärliga gränser för utbredningen",findGridLimits(analyzeGrid))

#Ett försök att skriva ut rätt grej. Lite copy-pasterisk på detta, men orka lära sig ett helt grafiskt framework

width, height = 400, 400
root = tk.Tk()
root.title("Sky")

frame = tk.Frame()
frame.pack()

canvas = tk.Canvas(frame, width=width, height=height)
for i in range(0,len(analyzeGrid)):
    x = analyzeGrid[i][0]
    y = analyzeGrid[i][1]
    canvas.create_rectangle(x,y,x+1,y+1)

canvas.pack()
root.mainloop()