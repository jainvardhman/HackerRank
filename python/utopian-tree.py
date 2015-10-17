INITIAL_HEIGHT = 1

def oddCycle(currentHt):
    return 2*currentHt

def evenCycle(currentHt):
    return currentHt + 1

def getHeightFromCycles(cycleCount):
    ht = INITIAL_HEIGHT
    cycleCount = cycleCount + 1
    for i in range (1,cycleCount):
        if i%2 == 0:
            ht = evenCycle(ht)
        else:
            ht = oddCycle(ht)
    return ht
        
n= int(input())
for i in range (0,n):
    heightOfTree = INITIAL_HEIGHT
    inp = int(input())
    if inp == 0:
        heightOfTree = heightOfTree   
    else:
        heightOfTree = getHeightFromCycles(inp)
        
    print(heightOfTree)
        
