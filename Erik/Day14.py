inputNum = 380621
#manuList = [3,8,6,2,1]
manuList = [5,1,5,8,9]



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



#print(cookList[-10:])
print(cookList[(recLimit):(recLimit+10)])





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

    if(manuList in cookList): #This does not work.
        print(i)
        break



























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