import re
with open("./inputsE/input09.txt","rt") as f:
    regSearch = re.search("([0-9]+) .+ ([0-9]+) .+", f.read())
    nrOfPlayers = int(regSearch.group(1))
    lastMarbleWorth = int(regSearch.group(2))
#nrOfPlayers = 13
#lastMarbleWorth = 7999
#print(nrOfPlayers)
#print(lastMarbleWorth)

playersList = [0]*nrOfPlayers
marbleRing = [0]
currentPos = 0
for i in range(1,lastMarbleWorth+1):  
    if(i%23 != 0):
        newPos = currentPos +2
        if(newPos > len(marbleRing)):
            newPos -= len(marbleRing)
        marbleRing.insert(newPos,i)
        currentPos = newPos
    else:
        activePlayer = i%nrOfPlayers
        playersList[activePlayer] += i
        currentPos = currentPos - 7
        if(currentPos < 0):
            currentPos = currentPos + len(marbleRing)
        playersList[activePlayer] += marbleRing.pop(currentPos)
    
print(max(playersList))


import collections as col
allPlayers = [0]*nrOfPlayers
bigMarblePoints = lastMarbleWorth * 100
#bigMarblePoints = 
activeMarble = 0
marbleCir = col.deque()
marbleCir.append(0)

for i in range(1,bigMarblePoints+1):
    if(i%23 != 0):
        marbleCir.rotate(-1)
        marbleCir.append(i)
    else:
        activePlayer = i%nrOfPlayers
        allPlayers[activePlayer] += i
        marbleCir.rotate(7)
        allPlayers[activePlayer] += marbleCir.pop()
        marbleCir.rotate(-1)

print(max(allPlayers))

