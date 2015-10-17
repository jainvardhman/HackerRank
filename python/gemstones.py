NRocks = 0
def initializeGlobals():
    global NRocks
    NRocks = int(input())

def findGems(rocks,minElsIndex):
    minElsRockUnique = set(list(rocks[minElsIndex]))
    cntGem = 0
    for el in minElsRockUnique:
        isGem = True
        for i in range(0,len(rocks)):
            if (i != minElsIndex):
                if not el in rocks[i]:
                    isGem = False
                    break
        if isGem:
            cntGem = cntGem + 1  
    return cntGem
            
        
    
def main():
    initializeGlobals()
    rocks = []    
    minElsIndex = 0
    for i in range(0,NRocks):
        rocks.append(input())
        if i == 0:
            minEls = len(rocks[i])
            minElsIndex = i
        else:
            if len(rocks[i]) < minEls:
                minEls = len(rocks[i])
                minElsIndex = i
    print(str(findGems(rocks,minElsIndex)))
        
main()