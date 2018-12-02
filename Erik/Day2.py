readFile = open("./inputsE/input02.txt","rt")
mainList = readFile.read().splitlines()
readFile.close()



#Day 2 part 1
def findDuplicates(searchStr):
    hasDouble = 0
    hasTriple = 0
    uglyList = [0]*27
    for i in range(0,len(searchStr)):
        uglyList[(ord(searchStr[i])-97)] += 1
    for j in range(0,len(uglyList)):
        if(uglyList[j] == 2):
            hasDouble = 1
        if(uglyList[j] == 3):
            hasTriple = 1
    return hasDouble, hasTriple


totalDoubles = 0
totalTriples = 0
for m in range(0,len(mainList)):
    tempCounter = findDuplicates(mainList[m])
    totalDoubles += tempCounter[0]
    totalTriples += tempCounter[1]

print("Found " +str(totalDoubles) +" doubles and " +str(totalTriples) +" triples. Checksum = " +str(totalDoubles * totalTriples))



#Day 2 part 2