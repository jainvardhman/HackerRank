testCases = 0

def initializeGlobals():
    global testCases
    testCases = int(input())
       
def getDiffBtwChars(WArray):
    lenWArrHalf = len(WArray)/2
    maxIndex = len(WArray) - 1
    charsSeen = 0
    diffChars = 0
    while(charsSeen < lenWArrHalf):
        diffChars = diffChars + abs(ord(WArray[maxIndex]) - ord(WArray[charsSeen]))
        maxIndex = maxIndex - 1
        charsSeen = charsSeen + 1
    return diffChars
        
def main():
    initializeGlobals()
    for i in range(0,testCases):
        letterW = input()
        WArray = list(letterW)
        print(getDiffBtwChars(WArray))
        
main()