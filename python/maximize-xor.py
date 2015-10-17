totalLanes = 0
testCases = 0
lanesWidth = []

def initializeGlobals():
    global totalLanes,testCases,lanesWidth
    totalLanes,testCases = input().split()
    totaLanes,testCases = int(totalLanes),int(testCases)
    lanesWidth = input().split()
    for i in range(0,len(lanesWidth)):
        lanesWidth[i] = int(lanesWidth[i])

def findMaxVehicleWidth(entry,exit):
    min = lanesWidth[entry]
    for i in range(entry,exit+1):
        if lanesWidth[i] < min:
            min = lanesWidth[i]
        else:
            min = min
    return min
        
def main():
    initializeGlobals()
    for i in range(0,testCases):
        entry,exit = input().split()
        entry,exit = int(entry),int(exit)
        print(str(findMaxVehicleWidth(entry,exit)))
        
main()