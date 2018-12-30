import re

#Läs filen, skriv till formatet [[Xstart,Xend,Ystart,Yend],[...]]
with open("./inputsE/input17.txt") as f:
    rawInput = f.read().splitlines()

waterStartPos = [500,0]
mudLocations = []
for i in range(0,len(rawInput)):
    coords = []
    regSearchX = re.search("x=[0-9]+\.?\.?[0-9]+",rawInput[i]).group(0)
    regSearchY = re.search("y=[0-9]+\.?\.?[0-9]+",rawInput[i]).group(0)
    getX = re.findall("[0-9]+", regSearchX)
    getY = re.findall("[0-9]+", regSearchY)
    if(len(getX) < 2):
        coords.append(int(getX[0]))
        coords.append(int(getX[0]))
    else:
        coords.append(int(getX[0]))
        coords.append(int(getX[1]))
    if(len(getY) < 2):
        coords.append(int(getY[0]))
        coords.append(int(getY[0]))
    else:
        coords.append(int(getY[0]))
        coords.append(int(getY[1]))
    mudLocations.append(coords)


#Extrafunktion för att leta gränser
def findExtremes(coordList):
    xVals = set() 
    yVals = set()
    [xVals.add(coordList[i][0]) for i in range(0,len(coordList))]
    [xVals.add(coordList[j][1]) for j in range(0,len(coordList))]
    [yVals.add(coordList[k][2]) for k in range(0,len(coordList))]
    [yVals.add(coordList[l][3]) for l in range(0,len(coordList))]
    return min(xVals), max(xVals), min(yVals), max(yVals)
    
print(findExtremes(mudLocations))


