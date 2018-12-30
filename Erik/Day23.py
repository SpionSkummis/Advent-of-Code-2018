import re
with open("./inputsE/input23.txt", "rt") as f:
    rawInput = f.read().splitlines()

#Gör om till lista, format [X,Y,Z,R]
inputList = []
for i in range(0,len(rawInput)):
    shortList = []
    regSearch = re.search("pos=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>, r=(-?[0-9]+)", rawInput[i])
    for j in range(1,5):
        shortList.append(int(regSearch.group(j)))
    inputList.append(shortList)
#print(inputList)


#Hitta störst radie!
sortedList = sorted(inputList,key=lambda x: x[3],reverse=True)

#Kolla avstånd mot alla andra bots, räkna de som är inom räckvidd genom att göra en lista?
#Först en funktion för att räkna manhattan mellan två punkter.
def findDist(x1,y1,z1,x2,y2,z2):
    return ((abs(x1-x2)) + (abs(y1-y2)) + (abs(z1-z2)))
#Och en funktion som kollar ifall prick ett når prick två
def isInRange(radius,x1,y1,z1,x2,y2,z2):
    if(((abs(x1-x2)) + (abs(y1-y2)) + (abs(z1-z2))) <= radius):
        return True
    return False

xPos = sortedList[0][0]
yPos = sortedList[0][1]
zPos = sortedList[0][2]
radius = sortedList[0][3]
nrInRange = 0
print(len(sortedList),sortedList[0:5])
for i in range(0,len(sortedList)): #Den egna ska inkluderas
    if(isInRange(radius,xPos,yPos,zPos,sortedList[i][0],sortedList[i][1],sortedList[i][2])):
        nrInRange += 1

print(nrInRange)
# 604 to low, men den ska räkna med sig själv?! så 605? Fast det är fel. Hittade felet, ett anrop till fel position i en lista #toksmart. Rätt på min input är 906

