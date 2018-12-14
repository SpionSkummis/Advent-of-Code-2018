with open("./inputsE/input13-t2.txt", "rt") as f:
    inputList = f.read().splitlines()

print(len(inputList))
print(len(inputList[0]))

# ^^^^vvvv<>>>>>>>>   -- ska vara alla vagnar i min input

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
        self.dir = startDir(startChar) # 0=N, 1=E, 2=S, 3=W.
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
            self.yPos += 1
        elif(self.dir == 1):
            self.xPos += 1
        elif(self.dir == 2):
            self.yPos -= 1
        elif(self.dir == 3):
            self.xPos -= 1


    def getpos(self):
        return self.xPos, self.yPos

    def intersection_turn(self):
        self.turnID = self.turns % 3
        if(self.turnID == 0):
            self.dir = (self.dir - 1)%4
        elif(self.turnID == 2):
            self.dir = (self.dir + 1)%4
        self.turns += 1


def replaceCarts(rawMap):
    replaceMap = [""]*len(rawMap)
    """for x in range(0,len(rawMap)):
        for y in range(0,len(rawMap[0])):
            if((rawMap[x][y] == "<") or (rawMap[x][y] == ">")):
                rawMap[x][y] = "-"
            if((rawMap[x][y] == "^") or (rawMap[x][y] == "v")):
                rawMap[x][y] = ("|")"""
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
            #print(inputList[x][y])
#Konverterar vagnar till spår
mainMap = replaceCarts(inputList)
#print(len(wagonList))


collision = False
colXY = (0,0)

tick = 0
while(not collision):
    print(tick)
    tick += 1
    for i in range(0,len(wagonList)):
        wagonList[i].move(mainMap)
        
    """for i in range(0,len(wagonList)):
        for j in range(i+1,len(wagonList)):
            if(wagonList[i].getpos() == wagonList[j].getpos()):
                collision = True
                colXY = wagonList[i].getpos()
                print("BOOM!")"""
    

print(tick)