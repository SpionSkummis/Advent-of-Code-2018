with open("./inputsE/input08.txt", "rt") as f:
    rawInput = f.read().strip("\n").split(" ")

inputList = []
for i in range(0,len(rawInput)):
    inputList.append(int(rawInput[i]))


def nodeLen(inList, pos):
    thisNodeLen = 0
    chSumSum = 0
    #Har den metadata, om ja, ta emot och skicka tillbaka
    #Om den har barn ska den anropa funktionen för barnet
    startPos = pos
    childNr = inList[startPos]
    metaLen = inList[startPos+1]
    if(childNr == 0):
        thisNodeLen = 2+metaLen
        chSumSum = sum(inList[startPos+2:startPos+2+metaLen])
        return (thisNodeLen,chSumSum)
    else:
        currPos = startPos + 2
        for i in range(0,childNr):
            tempCont = nodeLen(inList,currPos)
            currPos += tempCont[0]
            chSumSum += tempCont[1]
        chSumSum += sum(inList[currPos:currPos+metaLen])
        thisNodeLen = currPos + metaLen - startPos
    return (thisNodeLen,chSumSum)

print(nodeLen(inputList,0))
#50744 too high, 46829 rätt som fan



def partTwo(inList, pos):
    thisNodeLen = 0
    chSumSum = 0
    startPos = pos
    childNr = inList[startPos]
    metaLen = inList[startPos+1]
    if(childNr == 0):
        thisNodeLen = 2+metaLen
        chSumSum = sum(inList[startPos+2:startPos+2+metaLen])
        return (thisNodeLen,chSumSum)
    else:
        currPos = startPos + 2
        childList = [0]
        for i in range(0,childNr):
            tempCont = partTwo(inList,currPos)
            currPos += tempCont[0]
            childList.append(tempCont[1])
        for i in range(0,15):
            childList.append(0)
        metaNrs = inList[currPos:currPos+metaLen]
        for i in range(0,len(metaNrs)):
            chSumSum += childList[metaNrs[i]]
        thisNodeLen = currPos + metaLen - startPos

    return (thisNodeLen,chSumSum)

print(partTwo(inputList,0))

#36950 too low, 51656 too high, 37450 rätt som fan!