#Jens lösning för dag 1. Lite mindre kod, lite snyggare, (men färre for-loopar :(( )

mainList =[]
with open("./inputsE/input01.txt", "rt") as readFile:
    for line in readFile:
        mainList.append(int(line))

print(sum(mainList))