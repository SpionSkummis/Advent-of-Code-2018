with open("./inputsE/input12.txt", "rt") as f:
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

gardenNum = []
for i in range(0,len(rawGarden)):
    if(rawGarden[i] == "#"):
        gardenNum.append(1)
    else:
        gardenNum.append(0)

#Match, make, choose new one. Very verbose woo
currentGen = gardenNum.copy()
#Lägg till mer blankt utrymme i slutet
for i in range(0,250):
    currentGen.append(0)

#Lägg till mer i början
for i in range(0,10):
    currentGen.insert(0,0)

gens = 20
for i in range(0,gens):
    #print(sum(currentGen), i)
    nextGen = [0,0,0,0]
    for j in range(2,len(currentGen)-2):
        for n in range(0,len(instrNum)):
            if(currentGen[j-2:j+3] == instrNum[n][0:5]):
                nextGen.insert(j,instrNum[n][5])
    currentGen = nextGen #.copy() #Jag vet inte om copy behövs, det kanske sparar en massa konstiga referenser?
    #Kanske hjälper lite med minne och sånt?? del nextGen

print(len(currentGen))

#54 är feeeeeel, och 63 också. Kanske för att jag inte läste uppgiften ordentligt.

#Svaret till del ett
potSum = 0
for i in range(0,len(currentGen)):
    if(currentGen[i] == 1):
        potSum += (i-10)
print("Part one answ",potSum)



#Jag letar repetitioner! Börjar om från början
currentGen = gardenNum.copy()
for i in range(0,500):
    currentGen.append(0)
for i in range(0,10):
    currentGen.insert(0,0)

prevSeen = []
everyGarden = []

gens = 172
for i in range(0,gens):
    nextGen = [0,0,0,0]
    for j in range(2,len(currentGen)-2):
        for n in range(0,len(instrNum)):
            if(currentGen[j-2:j+3] == instrNum[n][0:5]):
                nextGen.insert(j,instrNum[n][5])
    shortList = nextGen[currentGen.index(1)-1:2+(len(currentGen))-(currentGen[::-1].index(1))]
    if(shortList in prevSeen):
        print("Found a duplicate at",i)
        #print(shortList)
    prevSeen.append(shortList.copy())
    currentGen = nextGen.copy()
    del shortList, nextGen


#Här är kod som kan hitta lösningen för del b med lite manuellt joxande.
"""
for a in range(0,len(everyGarden)):
    for b in range(0,len(everyGarden)):
        if(a != b):
            if(everyGarden[a] == everyGarden[b]):
                print("Number",a,"matches nr",b)
"""

#Den här delen skriver ut svaret till del ett, och hjälper till lite med del två
print(len(currentGen))
potSum = 0
for i in range(0,len(currentGen)):
    if(currentGen[i] == 1):
        potSum += (i-10)
print(gens,potSum)

#200 16113, 201 16188, 202 16263
#Någonstans kring 170 generationer börjar mönstret upprepa sig och ökar med 75 per generation...
print("200 -> 201 diff",(16188-16113))
print("201 -> 202 diff",(16263-16188))
print(((50000000000-201)*75)+16188)
