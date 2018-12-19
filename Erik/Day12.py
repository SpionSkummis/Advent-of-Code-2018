with open("./inputsE/input12.txt", "rt") as f:
#with open("./inputsE/Outputs/input12-test.txt", "rt") as f:
#with open("./inputsE/Outputs/input12-jens.txt", "rt") as f:
    rawGarden = f.readline().strip("inital state: ")
    rawInstructions = f.read().splitlines()
    rawInstructions.pop(0)

#Omvandla allt till fina ettor och nollor
instrNum = []
for i in range(0,len(rawInstructions)):
    tempList = []
    for j in range(0,5):
        if(rawInstructions[i][j] == "#"):
            tempList.append(1)
        else:
            tempList.append(0)
    if(rawInstructions[i][9] == "#"):
        tempList.append(1)
    else:
        tempList.append(0)
    instrNum.append(tempList)


print(rawGarden)
print(len(rawGarden))


#print(instrNum)

gardenNum = []
for i in range(0,len(rawGarden)):
    if(rawGarden[i] == "#"):
        gardenNum.append(1)
    else:
        gardenNum.append(0)

#Lägg till mer blankt utrymme, i slutet
for i in range(0,250):
    gardenNum.append(0)

#Lägg till mer i början
for i in range(0,10):
    gardenNum.insert(0,0)


firstPlantAt = []
#Match, make, choose new one. Very verbose woo
gens = 20
currentGen = gardenNum.copy()
print(len(currentGen))
for i in range(0,gens):
    #print(sum(currentGen), i)
    nextGen = [0,0,0,0]
    for j in range(2,len(currentGen)-2):
        for n in range(0,len(instrNum)):
            if(currentGen[j-2:j+3] == instrNum[n][0:5]):
                nextGen.insert(j,instrNum[n][5]) #append(instrNum[n][5])
    #nextGen.append(0)
    #nextGen.append(0)
    currentGen = nextGen.copy()
    del nextGen


print(len(currentGen))
print(sum(currentGen))

#54 är feeeeeel, och 63 också.

potSum = 0
for i in range(0,len(currentGen)):
    if(currentGen[i] == 1):
        potSum += (i-10)
print(potSum)


#How bowt samma sak fast med dictionary?

