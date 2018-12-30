#Jens lösning för dag 1. Lite mindre kod, lite snyggare, (men färre for-loopar :(( )
#Set istället för list i lösning två, och mycket mindre kladd.
#Så mycket lättare att använda ints som ints och inte som strings #genombrott #prohacker

mainList =[]
with open("./inputsE/input01.txt", "rt") as readFile:
    for line in readFile:
        mainList.append(int(line))

print("Final freq afer one run: " +str(sum(mainList)))

freqFound = False
currentFreq = 0
seenFreqs = set()
seenFreqs.add(currentFreq)
while(not freqFound):
    for i in range(0,len(mainList)):
        currentFreq += mainList[i]
        if(currentFreq in seenFreqs):
            freqFound = True
            print("First repeated freq: " +str(currentFreq))
            break
        seenFreqs.add(currentFreq)
