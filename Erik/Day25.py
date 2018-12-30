with open("./inputsE/input25.txt","rt") as f:
    rawInput = f.read().splitlines()

#Gör input till en lista med tuples
inputList = []
for i in range(0,len(rawInput)):
    tempTupe = (int(rawInput[i].split(",")[0]),int(rawInput[i].split(",")[1]),int(rawInput[i].split(",")[2]),int(rawInput[i].split(",")[3]))
    inputList.append(tempTupe)

def distCalcTest(x1,y1,z1,t1,x2,y2,z2,t2):
    return ((abs(x1-x2)+abs(y1-y2)+abs(z1-z2)))

def distCalc(tup1,tup2):
    xDist = abs(tup1[0]-tup2[0])
    yDist = abs(tup1[1]-tup2[1])
    zDist = abs(tup1[2]-tup2[2])
    tDist = abs(tup1[3]-tup2[3])
    return xDist + yDist + zDist + tDist


tempList = inputList.copy()
consts = []
rounds = 0

while(len(tempList) > 0):

    roundSet = set()
    for i in range(len(tempList)-1,-1,-1):
        if(distCalc(tempList[-1],tempList[i]) < 4):
            roundSet.add(tempList[i])

    if(len(roundSet) > 1):
        keeprunning = True
        while(keeprunning):
            startLen = len(roundSet)
            tempSet = set()
            for node in roundSet:
                for i in range(0,len(tempList)):
                    if(distCalc(node,tempList[i]) < 4):
                        tempSet.add(tempList[i])
            roundSet.update(tempSet)
            if(len(roundSet) == startLen):
                keeprunning = False
    consts.append(roundSet)
    for item in roundSet:
        tempList.remove(item)




print(len(consts))
#print(consts)






