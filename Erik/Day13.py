with open("./inputsE/input13.txt", "rt") as f:
    inputList = f.read().splitlines()

# ^^^^vvvv<>>>>>>>>   -- ska vara alla vagnar i min input 17st - 8 krockar

def startDir(startChar):
    if(startChar == "^"):
        return  0
    elif(startChar == ">"):
        return  1
    elif(startChar == "v"):
        return  2
    elif(startChar == "<"):
        return  3
    else:
        print("Error in startDir function")

class Cart:
    def __init__(self,xPos,yPos,startChar): #StartChar?
        self.xPos = xPos
        self.yPos = yPos
        self.dir = 8
        self.dir = startDir(startChar) # 0=N, 1=E, 2=S, 3=W. Also x+ v, y+ ->
        self.turns = 0

#    def startDir(self, startChar):
#        if(startChar == "^"):
#            return  0
#        elif(startChar == ">"):
#            return  1
#        elif(startChar == "v"):
#            return  2
#        else:
#            return  3
            

    def move(self, mainMap):
        posChar = mainMap[self.xPos][self.yPos]

        if(posChar == "\\"):
            if(self.dir == 0):
                self.dir = 3
            elif(self.dir == 1):
                self.dir = 2
            elif(self.dir == 2):
                self.dir = 1
            elif(self.dir == 3):
                self.dir = 0

        elif(posChar == "/"):
            if(self.dir == 0):
                self.dir = 1
            elif(self.dir == 1):
                self.dir = 0
            elif(self.dir == 2):
                self.dir = 3
            elif(self.dir == 3):
                self.dir = 2
        
        elif(posChar == "+"):
            self.intersection_turn()

        elif(posChar == " "):
            print("Possible error at:",self.xPos,self.yPos)

        if(self.dir == 0):
            self.xPos -= 1
        elif(self.dir == 1):
            self.yPos += 1
        elif(self.dir == 2):
            self.xPos += 1
        elif(self.dir == 3):
            self.yPos -= 1


    def getpos(self):
        return self.yPos, self.xPos

    def intersection_turn(self):
        self.turnID = self.turns % 3
        if(self.turnID == 0):
            self.dir = (self.dir - 1)%4
        elif(self.turnID == 2):
            self.dir = (self.dir + 1)%4
        self.turns += 1


def replaceCarts(rawMap):
    replaceMap = [""]*len(rawMap)
    for i in range(0,len(rawMap)):
        step1 = rawMap[i].replace("<","-")
        step2 = step1.replace(">","-")
        step3 = step2.replace("^","|")
        replaceMap[i] = step3.replace("v","|")
    return replaceMap.copy()



#Skapa en lista med alla vagnar
wagonList = []
for x in range(0,len(inputList)):
    for y in range(0,len(inputList[0])):
        if((inputList[x][y] == ">") or (inputList[x][y] == "<") or (inputList[x][y] == "v") or (inputList[x][y] == "^")):
            wagonList.append(Cart(x,y,inputList[x][y]))

#Konverterar vagnar till spår
mainMap = replaceCarts(inputList)

collision = False
colXY = (0,0)
tick = 0
while(not collision):
    tick += 1
    for i in range(0,len(wagonList)):
        wagonList[i].move(mainMap)
        
    for i in range(0,len(wagonList)):
        for j in range(i+1,len(wagonList)):
            if(wagonList[i].getpos() == wagonList[j].getpos()):
                collision = True
                colXY = wagonList[i].getpos()
                #print("BOOM!")
    

print("After",tick,"rounds, the first colision was at", colXY)




mainMap2 = replaceCarts(inputList)
wagonList2 = []
for x in range(0,len(inputList)):
    for y in range(0,len(inputList[0])):
        if((inputList[x][y] == ">") or (inputList[x][y] == "<") or (inputList[x][y] == "v") or (inputList[x][y] == "^")):
            wagonList2.append(Cart(x,y,inputList[x][y]))


tick = 0
while(len(wagonList2) > 1):
    tick += 1
    collidedCarts = []

    for i in range(0,len(wagonList2)):
        wagonList2[i].move(mainMap2)

    for i in range(0,len(wagonList2)):
        for j in range(0,len(wagonList2)):
            if((wagonList2[i].getpos() == wagonList2[j].getpos()) and (i != j)):
                print("collision detected at", wagonList2[i].getpos(), wagonList2[j].getpos(), "tick", tick, i, j)
                if(i not in collidedCarts):
                    collidedCarts.append(i)
                if(j not in collidedCarts):
                    collidedCarts.append(j)
        
    collidedCarts.sort()
    for i in range(len(collidedCarts)-1,-1,-1):
        print(wagonList2[collidedCarts[i]].getpos(),tick,collidedCarts[i])
        wagonList2.pop(collidedCarts[i])



    
    
    """
    if(len(collidedCarts) > 0):
        print(collidedCarts.sort())

        
    collidedCarts.sort()
    for i in range(len(collidedCarts)-1, 0, -1):
        
        print("BOOM!",wagonList2[collidedCarts[i]].getpos(), "tick", tick)
        wagonList2.pop(collidedCarts[i])
    """
#wagonList2[0].move(mainMap2)
print(wagonList2[0].getpos())
print(tick)

#print(colXY)




#Test (73,134) - fel (87,11) - fel (86,11) - fel