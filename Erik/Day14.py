inputNum = 380621
manuList = [3,8,0,6,2,1]
#manuList = [5,1,5,8,9]
#manuList = [9,2,5,1,0]
#manuList = [5,9,4,1,4]



cookList = [3,7]
elf1Pos = 0
elf2Pos = 1
recLimit = inputNum


for i in range(0,recLimit+10):
    scoreSum = cookList[elf1Pos] + cookList[elf2Pos]
    if(scoreSum > 9):
        cookList.append(scoreSum//10)
        cookList.append(scoreSum%10)
    else:
        cookList.append(scoreSum)
    elf1Pos = (elf1Pos +1 + cookList[elf1Pos]) % (len(cookList))
    elf2Pos = (elf2Pos +1 + cookList[elf2Pos]) % (len(cookList))



print(cookList[-10:])
print(cookList[(recLimit):(recLimit+10)])





cookList = [3,7]
elf1Pos = 0
elf2Pos = 1
recLimit = inputNum
lastAddIsDual = False
patternFound = False
while(not patternFound):
#for i in range(0,recLimit+10):
    scoreSum = cookList[elf1Pos] + cookList[elf2Pos]
    if(scoreSum > 9):
        cookList.append(scoreSum//10)
        cookList.append(scoreSum%10)
        if(cookList[-6:] == manuList or cookList[-7:-1] == manuList):
            if(cookList[-7:-1] == manuList):
                lastAddIsDual = True
            print("hopp")
            patternFound = True
    else:
        cookList.append(scoreSum)
        if(cookList[-6:] == manuList):
            patternFound = True
    elf1Pos = (elf1Pos +1 + cookList[elf1Pos]) % (len(cookList))
    elf2Pos = (elf2Pos +1 + cookList[elf2Pos]) % (len(cookList))

    
subtractNum = 6
if(lastAddIsDual):
    subtractNum += 1
print(len(cookList)-subtractNum)

#38052 - too low 20182291 - too high
























"""
for i in range(0,19):
    scoreSum = cookList[elf1Pos] + cookList[elf2Pos]
    if(scoreSum > 9):
        cookList.append(scoreSum//10)
        cookList.append(scoreSum%10)
    else:
        cookList.append(scoreSum)
    elf1Pos = (elf1Pos +1 + cookList[elf1Pos]) % (len(cookList))
    elf2Pos = (elf2Pos +1 + cookList[elf2Pos]) % (len(cookList))
    print(cookList)
    print(elf1Pos,elf2Pos)
#print(cookList[9])
"""