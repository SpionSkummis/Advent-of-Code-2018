import re
with open("./inputsE/input09.txt","rt") as f:
    regSearch = re.search("([0-9]+) .+ ([0-9]+) .+", f.read())
    nrOfPlayers = int(regSearch.group(1))
    lastMarbleWorth = int(regSearch.group(2))
#nrOfPlayers = 13
#lastMarbleWorth = 7999
#print(nrOfPlayers)
#print(lastMarbleWorth)
#lastMarbleWorth = lastMarbleWorth*100
playersList = [0]*nrOfPlayers
marbleRing = [0]
currentPos = 0
for i in range(1,lastMarbleWorth+1):
    activePlayer = i%nrOfPlayers
    if(i%23 != 0):
        newPos = currentPos +2
        if(newPos > len(marbleRing)):
            newPos -= len(marbleRing)
        marbleRing.insert(newPos,i)
        currentPos = newPos
    else:
        #print(i)
        playersList[activePlayer] += i
        #print(playersList[activePlayer])
        currentPos = currentPos - 7
        if(currentPos < 0):
            currentPos = currentPos + len(marbleRing)
        #print(currentPos, "currentpos")
        #print(marbleRing[currentPos], "val marblering currentpos")
        playersList[activePlayer] += marbleRing.pop(currentPos)
    #print(activePlayer)
    
print(max(playersList))
#print(playersList)