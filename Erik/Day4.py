import re

inputList = []
with open("./inputsE/input04.txt", "rt") as f:
    inputList = f.read().splitlines()
inputList.sort()

"""
#Kontrollutskrift för att det ät ball och för att lättare kolla vad jag jobbar med
with open("./inputsE/Outputs/output04.txt", "wt") as f:
    for i in range(0,len(inputList)):
        f.write(str(inputList[i]) +"\n")
"""

"""
#Kollar för dubletter för att säkerställa att sorteringen fungerat som den ska
for i in range(0,len(rawInputList)):
    for j in range (i+1,len(rawInputList)):
        if(re.search("\[.+\]", rawInputList[i]).group(0) == re.search("\[.+\]", rawInputList[j]).group(0)):
            print("Duplicate date at: " +str(i))
"""
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
print("The sleepiest guard is " +sleepyGuardId +" who slept " +str(sleepyGuardTime) +" minutes")

for key, v in guardDict.items():
    print(key+" " +str(v))


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
print(guardSleepHour)
for i in range(0, len(guardSleepHour)):
    print("Minut nr " +str(i) +": " +str(guardSleepHour[i]))

stupidList =[]
for key in guardDict:
    guardDict[key] = [0]*60
#print(guardDict)


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


print(type(guardDict["Guard #313"]))
print(max(guardDict["Guard #313"]))
print(type(max(guardDict["Guard #313"])))


for key in guardDict:
    if(max(guardDict[key]) > valMax):
        valMax = max(guardDict[key])
        keyMax = key

print(keyMax)
print(valMax)
#print(guardDict[keyMax])

for i in range(0, len(guardDict[keyMax])):
    print("Minut nr " +str(i) +": " +str(guardDict[keyMax][i]))