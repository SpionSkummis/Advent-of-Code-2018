import re

inputList = []
with open("./inputsE/input04.txt", "rt") as f:
    inputList = f.read().splitlines()
inputList.sort()

"""
#Kontrollutskrift för att det är ball och för att lättare kolla vad jag jobbar med
with open("./inputsE/Outputs/output04.txt", "wt") as f:
    for i in range(0,len(inputList)):
        f.write(str(inputList[i]) +"\n")
#Kollar för dubletter för att säkerställa att sorteringen fungerat som den ska
for i in range(0,len(rawInputList)):
    for j in range (i+1,len(rawInputList)):
        if(re.search("\[.+\]", rawInputList[i]).group(0) == re.search("\[.+\]", rawInputList[j]).group(0)):
            print("Duplicate date at: " +str(i))
"""

#Formaterar listan till instruktioner
def sleepyParser(rawList):
    parsedList = []
    for i in range(0,len(rawList)):
        tempList = []
        tempList.append()

#Skapar dictionary med alla vakter, i övrigt tom
guardDict = {}
for i in range(0,len(inputList)):
    if(re.search("Guard #[0-9]+", inputList[i])):
        tempGuardId = re.search("Guard #[0-9]+", inputList[i]).group(0)
        if(tempGuardId not in guardDict):
            guardDict[tempGuardId] = 0

#Går igenom instruktionerna, lägger till tid när vakten sover??
currentGuard = ""
for i in range(0,len(inputList)):
    if(re.search("Guard #[0-9]+", inputList[i])):
        currentGuard = re.search("Guard #[0-9]+", inputList[i]).group(0)
    elif(re.search("falls", inputList[i])):
        fellAsleep = int(re.search(":([0-9]+)", inputList[i]).group(1))
    elif(re.search("wakes", inputList[i])):
        wokeUp = int(re.search(":([0-9]+)", inputList[i]).group(1))
        timeSlept = wokeUp-fellAsleep
        guardDict[currentGuard] += timeSlept

#Hittar största värdet?
sleepyGuardId = ""
sleepyGuardTime = 0
for i in guardDict:
    if(sleepyGuardTime < guardDict[i]):
        sleepyGuardId = i
        sleepyGuardTime = guardDict[i]
print("The sleepiest guard is " +sleepyGuardId +" who slept " +str(sleepyGuardTime) +" minutes.")

guardSleepHour = [0]*60
currentGuard = ""
for i in range(0,len(inputList)):
    if(re.search("Guard #[0-9]+", inputList[i])):
        currentGuard = re.search("Guard #[0-9]+", inputList[i]).group(0)
    elif(re.search("falls", inputList[i]) and (currentGuard == sleepyGuardId)):
        fellAsleep = int(re.search(":([0-9]+)", inputList[i]).group(1))
    elif(re.search("wakes", inputList[i]) and (currentGuard == sleepyGuardId)):
        wokeUp = int(re.search(":([0-9]+)", inputList[i]).group(1))
        for j in range(fellAsleep,wokeUp):
            guardSleepHour[j] += 1

sleepyMin = 0
sleepyMinId = 0
for i in range(0, len(guardSleepHour)):
    if(guardSleepHour[i] > sleepyMin):
        sleepyMin = guardSleepHour[i]
        sleepyMinId = i
print("Sover oftast minut nummer " +str(sleepyMinId) +" (" +str(sleepyMin) +" minuter). Svaret på uppg1 är därför " +str(int(re.search("[0-9]+",sleepyGuardId).group(0)) * sleepyMinId))

stupidList =[]
for key in guardDict:
    guardDict[key] = [0]*60

currentGuard = ""
for i in range(0,len(inputList)):
    if(re.search("Guard #[0-9]+", inputList[i])):
        currentGuard = re.search("Guard #[0-9]+", inputList[i]).group(0)
    elif(re.search("falls", inputList[i])):
        fellAsleep = int(re.search(":([0-9]+)", inputList[i]).group(1))
    elif(re.search("wakes", inputList[i])):
        wokeUp = int(re.search(":([0-9]+)", inputList[i]).group(1))
        for j in range(fellAsleep,wokeUp):
            guardDict[currentGuard][j] += 1

keyMax = ""
valMax = int(0)
for key in guardDict:
    if(max(guardDict[key]) > valMax):
        valMax = max(guardDict[key])
        keyMax = key

mostSleptMinuteId = 0
for i in range(0,len(guardDict[keyMax])):
    if(guardDict[keyMax][i] == valMax):
        mostSleptMinuteId = i

print(keyMax +" sov mest under samma minut, nämligen minut " +str(mostSleptMinuteId) +". Svaret är därför " +str(int(re.search("[0-9]+", keyMax).group(0)) * mostSleptMinuteId))
