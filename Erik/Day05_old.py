
with open("./inputsE/input05.txt", "rt") as f:
    inputString = f.read().strip("\n")

#Bra lädromar: i en for-loop beräknas "range" direkt och inte efter varje varv.
#Strings i python går inte att ändra i på ett bra sätt.
"""for i in range(0, (len(inputList) -45000)):
    if((ord(inputList[i]) == (ord(inputList[i+1]) + 32)) or (ord(inputList[i]) == (ord(inputList[i+1]) - 32))):
        inputList[i:(i+2)] = []
        #i -= 1"""

#Testcase
#inputString = "dabAcCaCBAcCcaDA"

#Day1
day1List = list(inputString)
i = 0
while(i < (len(day1List)-1)):
    if((ord(day1List[i]) == (ord(day1List[i+1]) + 32)) or (ord(day1List[i]) == (ord(day1List[i+1]) - 32))):
        day1List[i:(i+2)] = []
        if(i>0):
            i -= 1
    else:
        i +=1

print(len(day1List))

#Day 2, slow :/
def charRemover(string, int):
    workerList = list(string)
    i = 0
    while(i < len(workerList)):
        if((workerList[i] == chr(int+97)) or (workerList[i] == chr(int+65))):
            workerList.pop(i)
        else:
            i += 1
    return workerList


listOfFinalLengts = [0]*26

i = 0
j = 0
for m in range(0,len(listOfFinalLengts)):
    noCharList = charRemover(inputString,m)
    while(i < (len(noCharList)-1)):
        if((ord(noCharList[i]) == (ord(noCharList[i+1]) + 32)) or (ord(noCharList[i]) == (ord(noCharList[i+1]) - 32))):
            noCharList[i:(i+2)] = []
            if(i>0):
                i -= 1
        else:
            i +=1
    listOfFinalLengts[m] = len(noCharList)
    i = 0

listOfFinalLengts.sort()
print(listOfFinalLengts[0])
