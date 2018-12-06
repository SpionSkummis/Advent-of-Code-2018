
with open("./inputsE/input06.txt", "rt") as f:
    rawList = f.readlines()
    inputList = []
    for i in range(0,len(rawList)):
        inputList.append(rawList[i].strip("\n").split(", "))
        for i in range(0,len(inputList)):
            inputList[i][0] = int(inputList[i][0])
            inputList[i][1] = int(inputList[i][1])

print(inputList)
print(len(inputList))