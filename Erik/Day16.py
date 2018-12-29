import re

mainList = []
with open("./inputsE/input16.txt","rt") as f:
    for i in range(0,(3260//4)):
        sl = []
        for j in range(0,3):
            l = f.readline()
            reg = re.findall("[0-9]+",l)
            reg = [int(i) for i in reg]
            sl.append(reg)
        mainList.append(sl)
        k = f.readline()
testList = [[3,2,1,1],[9,2,1,2],[3,2,2,1]]

#Alla funktioner på en liten liten rad
# addr (add register) stores into register C the result of adding register A and register B.
def addr(regIn, instr):
    reg = regIn.copy()
    reg[instr[3]] = reg[instr[1]] + reg[instr[2]]
    return reg.copy()
# addi (add immediate) stores into register C the result of adding register A and value B.
def addi(regIn, instr):
    reg = regIn.copy()
    reg[instr[3]] = reg[instr[1]] + instr[2]
    return reg.copy()
# mulr (multiply register) stores into register C the result of multiplying register A and register B.
def mulr(regIn, instr):
    reg = regIn.copy()
    reg[instr[3]] = reg[instr[1]] * reg[instr[2]]
    return reg.copy()
# muli (multiply immediate) stores into register C the result of multiplying register A and value B.
def muli(regIn, instr):
    reg = regIn.copy()
    reg[instr[3]] = reg[instr[1]] * instr[2]
    return reg
# banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
def banr(regIn, instr):
    reg = regIn.copy()
    reg[instr[3]] = reg[instr[1]] & reg[instr[2]]
    return reg
# bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
def bani(regIn, instr):
    reg = regIn.copy()
    reg[instr[3]] = reg[instr[1]] & instr[2]
    return reg
# borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
def borr(regIn, instr):
    reg = regIn.copy()
    reg[instr[3]] = reg[instr[1]] | reg[instr[2]]
    return reg
# bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
def bori(regIn, instr):
    reg = regIn.copy()
    reg[instr[3]] = reg[instr[1]] & instr[2]
    return reg
# setr (set register) copies the contents of register A into register C. (Input B is ignored.)
def setr(regIn, instr):
    reg = regIn.copy()
    reg[instr[3]] = reg[instr[1]]
    return reg
# seti (set immediate) stores value A into register C. (Input B is ignored.)
def seti(regIn, instr):
    reg = regIn.copy()
    reg[instr[3]] = instr[1]
    return reg
# gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
def gtir(regIn, instr):
    reg = regIn.copy()
    if(instr[1] > reg[instr[2]]):
        reg[instr[3]] = 1
    else:
        reg[instr[3]] = 0
    return reg
# gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
def gtri(regIn, instr):
    reg = regIn.copy()
    if(reg[instr[1]] > instr[2]):
        reg[instr[3]] = 1
    else:
        reg[instr[3]] = 0
    return reg
# gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
def gtrr(regIn, instr):
    reg = regIn.copy()
    if(reg[instr[1]] > reg[instr[2]]):
        reg[instr[3]] = 1
    else:
        reg[instr[3]] = 0
    return reg
# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
def eqir(regIn, instr):
    reg = regIn.copy()
    if(instr[1] == reg[instr[2]]):
        reg[instr[3]] = 1
    else:
        reg[instr[3]] = 0
    return reg
# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
def eqri(regIn, instr):
    reg = regIn.copy()
    if(reg[instr[1]] == instr[2]):
        reg[instr[3]] = 1
    else:
        reg[instr[3]] = 0
    return reg
# eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
def eqrr(regIn, instr):
    reg = regIn.copy()
    if(reg[instr[1]] == reg[instr[2]]):
        reg[instr[3]] = 1
    else:
        reg[instr[3]] = 0
    return reg
# Ett tappert försök att göra alla lösningar och lägga dem i en lista. Skoj skoj.
def solveAll(startRegister, instructionSet):
    r = startRegister
    i = instructionSet
    answList = [addr(r,i),addi(r,i),mulr(r,i),muli(r,i),banr(r,i),bani(r,i),borr(r,i),bori(r,i),setr(r,i),seti(r,i),gtir(r,i),gtri(r,i),gtrr(r,i),eqir(r,i),eqri(r,i),eqrr(r,i)]
    return answList

def actsLike(inList):
    allCommands = ["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]
    solutions = solveAll(inList[0],inList[1])
    retThis = []
    for i in range(0,len(solutions)):
        #print(solutions[i], inList[2])
        if(solutions[i] == inList[2]):
            retThis.append(allCommands[i])
    return retThis

print
        

        



#Loopen som löser del 1 (651)
part1answ = 0
for i in range(0,len(mainList)):
    counter = 0
    solvedList = solveAll(mainList[i][0],mainList[i][1])
    for j in range(0,len(solvedList)):
        if(solvedList[j] == mainList[i][2]):
            counter += 1
    if(counter >= 3):
        part1answ += 1
print(part1answ)




#print(actsLike(testList))
allOpCodes = [["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]]*16
#print(allOpCodes)
for i in range(0,len(mainList)):
    thisOpCode = mainList[i][1][0]
    #print(thisOpCode)
    possibleCodes = actsLike(mainList[i])
    #print(possibleCodes)
    newList = []
    for j in range(0,len(possibleCodes)):
        if(possibleCodes[j] in allOpCodes[thisOpCode]):
            newList.append(possibleCodes[j])
    allOpCodes[thisOpCode] = newList.copy()

opDict = dict()
"""
for i in range(0,len(allOpCodes)):
    opDict[i] = allOpCodes[i]
"""

doneDict = dict()
done = False
while(not done):
    for i in range(0,len(allOpCodes)):
        removeKey = ""
        if(len(allOpCodes[i]) == 1):
            opDict[i] = allOpCodes[i][0]
            removeKey = allOpCodes[i][0]
            for j in range(0,len(allOpCodes)):
                if(removeKey in allOpCodes[j]):
                    allOpCodes[j].remove(removeKey)
    c = 0
    for i in range(0,len(allOpCodes)):
        if(len(allOpCodes[i]) == 0):
            c += 1
    if(c >= 8):
        done = True
    print(allOpCodes)

print(allOpCodes)
print(opDict)
"""
#completedInstr:
for i in range(0,len(allOpCodes)):
    if(len(allOpCodes[i]) == 0):
        completedInstr.append(allOpCodes[i][0])
        newList = []
        for j in range(0,len(allOpCodes)):
            pass
            
"""


for i in range(0,len(allOpCodes)):
    print(i, allOpCodes[i])



