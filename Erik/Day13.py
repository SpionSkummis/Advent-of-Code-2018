with open("./inputsE/input13.txt", "rt") as f:
    inputList = f.read().splitlines()

print(len(inputList))
print(len(inputList[0]))

class Cart:
    def __init__(self,xPos,yPos,direction): #StartChar?
        self.xPos = xPos
        self.yPos = yPos
        self.dir = direction # 0=N, 1=E, 2=S, 3=W.
        self.turns = 0

    def start_direction(self, startChar):
        if(startChar == "^"):
            self.dir = 0
        elif(startChar == ">"):
            self.dir = 1
        elif(startChar == "v"):
            self.dir = 2
        else:
            

    def move

    def getpos(self):
        return xPos, yPos

    def intersection_turn(self):
        self.turnID = self.turns % 3
        if(self.turnID == 0):
            self.dir = (self.dir - 1)%4
        elif(self.turnID == 2):
            self.dir 0 (self.dir + 1)%4
        self.turns += 1


