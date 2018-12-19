with open("./inputsE/input12.txt", "rt") as f:
    rawGarden = f.readline().strip("inital state: ")
    rawInstructions = f.read().splitlines()
    rawInstructions.pop(0)

print(rawGarden)