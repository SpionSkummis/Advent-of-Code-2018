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






print(testList)



# addr (add register) stores into register C the result of adding register A and register B.
def addr(reg, instr):
    reg[instr[3]] = reg[instr[1]] + reg[instr[2]]
    return reg
# addi (add immediate) stores into register C the result of adding register A and value B.
def addi(reg, instr):
    reg[instr[3]] = reg[instr[1]] + instr[2]
    return reg
# mulr (multiply register) stores into register C the result of multiplying register A and register B.
def mulr(reg, instr):
    reg[instr[3]] = reg[instr[1]] * reg[instr[2]]
    return reg
# muli (multiply immediate) stores into register C the result of multiplying register A and value B.
def muli(reg, instr):
    reg[instr[3]] = reg[instr[1]] * instr[2]
    return reg
# banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
def banr(reg, instr):
    reg[instr[3]] = reg[instr[1]] & reg[instr[2]]
    return reg
# bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
def bani(reg, instr):
    reg[instr[3]] = reg[instr[1]] & instr[2]
    return reg
# borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
def borr(reg, instr):
    reg[instr[3]] = reg[instr[1]] | reg[instr[2]]
    return reg
# bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
def bori(reg, instr):
    reg[instr[3]] = reg[instr[1]] & instr[2]
    return reg
# setr (set register) copies the contents of register A into register C. (Input B is ignored.)
def setr(reg, instr):
    reg[instr[3]] = reg[instr[1]]
    return reg
# seti (set immediate) stores value A into register C. (Input B is ignored.)
def seti(reg, instr):
    reg[instr[3]] = instr[1]
    return reg
# gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
def gtir(reg, instr):
    if(instr[1] > reg[instr[2]]):
        reg[instr[3]] = 1
    else:
        reg[instr[3]] = 0
    return reg
# gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
def gtri(reg, instr):
    if(reg[instr[1]] > instr[2]):
        reg[instr[3]] = 1
    else:
        reg[instr[3]] = 0
    return reg
# gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
def gtrr(reg, instr):
    if(reg[instr[1]] > reg[instr[2]]):
        reg[instr[3]] = 1
    else:
        reg[instr[3]] = 0
    return reg
# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
def eqir(reg, instr):
    if(instr[1] == reg[instr[2]]):
        reg[instr[3]] = 1
    else:
        reg[instr[3]] = 0
    return reg
# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
def eqri(reg, instr):
    if(reg[instr[1]] == instr[2]):
        reg[instr[3]] = 1
    else:
        reg[instr[3]] = 0
    return reg
# eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
def eqrr(reg, instr):
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

print(solveAll(testList[0],testList[1]))
