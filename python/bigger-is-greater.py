nStrings = 0
inputs = []
outputs = []

def rev(text):
    if len(text) <=1:
        return text
    else:
        return rev(text[1:]) + text[0]

def setGlobalInputs():
    global nStrings
    global inputs
    nStrings = int (input())
    for i in range(0,nStrings):
        inputs.append(input())

def findNextLexString(inp):
    revInp = list(rev(inp))
    revd = 0
    impossible = 1
    for x in range(0,len(revInp)):
        if ord(revInp[len(revInp)-1]) < ord(revInp[x]) and impossible == 1:
            impossible = 0
        if(ord(revInp[0]) > ord(revInp[x])):
            temp = revInp[x]
            revInp[x] = revInp[0]
            revInp[0] = temp
            revd = 1
            break
        else:
            continue
    if revd == 1:
        return rev(''.join(revInp))
    elif (impossible == 1):
        return "no answer"
    else:
        sortInp = list(inp[1:len(inp)])
        sortInp.sort()
        sortInp = list(inp[0] + ''.join(sortInp))
        for x in range(1,len(sortInp)-1):
            if ord(sortInp[0]) < ord(sortInp[x]):
                temp = sortInp[x]
                sortInp[x] = sortInp[0]
                sortInp[0] = temp
                break
        return (''.join(sortInp))
    
    
def main():
    global nStrings
    global inputs
    global outputs
    setGlobalInputs()
    for i in range(0,nStrings):
        #outputs.append(findNextLexString(inputs[i]))
        print(findNextLexString(inputs[i]))
        
main()