
with open("./inputsE/input08.txt", "rt") as f:
    rawInput = f.read().strip("\n").split(" ")
inputList = []
for i in range(0,len(rawInput)):
    inputList.append(int(rawInput[i]))


print(inputList)

class node:
    id = "???"

