import re

file_input = open("./inputsE/input01.txt", "rt")
mainString = file_input.read()
file_input.close()

listTest = mainString.split("\n")
listTest = listTest[:-1]

currentFreq = 0
beenHereBefore = []
for i in range(0,len(listTest)):
    currChange = listTest[i]
    if(currChange.startswith("+")):
        listElement = str(re.search("\d+", currChange).group(0))
        changeNum = int(listElement)
        currentFreq += changeNum
        beenHereBefore.append(currentFreq)

    elif(currChange.startswith("-")):
        listElement = str(re.search("\d+", currChange).group(0))
        changeNum = int(listElement)
        currentFreq -= changeNum
        beenHereBefore.append(currentFreq)

    else:
        print("Error! " +str(i))

print("Freq: " +str(currentFreq))



#Dag 2. Hysteriskt långsam kod som måste fixas
totalCounter = 0
duplicateFound = False
while(not duplicateFound):
    for i in range(0,len(listTest)):
        currChange = listTest[i]
        totalCounter += 1
        if(currChange.startswith("+")):
            listElement = re.search("\d+", currChange).group(0)
            changeNum = int(listElement)
            currentFreq += changeNum
            if(currentFreq in beenHereBefore):
                print("Reached " +str(currentFreq) +" in cycle " +str(i))
                duplicateFound = True
                break
            beenHereBefore.append(currentFreq)

        elif(currChange.startswith("-")):
            listElement = re.search("\d+", currChange).group(0)
            changeNum = int(listElement)
            currentFreq -= changeNum
            if(currentFreq in beenHereBefore):
                print("Reached " +str(currentFreq) +" in cycle " +str(i))
                duplicateFound = True
                break
            beenHereBefore.append(currentFreq)

        else:
            print("Error! " +str(i))