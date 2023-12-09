def readFile(fileLocation):
    lines=[]
    with open(fileLocation, 'r') as fileobj:
        for row in fileobj:
            row=row.rstrip('\n')
            lines.append(row)
    
    return lines

def getCardList(line, isWinning):
    #Split into Winning 
    winningList=line.split(" | ")[isWinning]
    winningList=winningList.replace("  "," 0")
    if(winningList[0]==" "):
        winningList=winningList.replace(" ","0",1)
        
    winningList=winningList.split(" ")
    return winningList

def getNumberOfWins(winningList,drawnList):
    sum=0
    for val in winningList:        
        sum+=drawnList.count(val)
    
    if sum==0:
        return 0
    else:
        return 2**(sum-1)
    
        
def getSumOfValues(linesFromFile):
    
    totalSum=0
    for line in linesFromFile:
        #Split into Card 
        cardNum=line.split(": ")[0]
        
        line=line.split(": ")[1]
        
        #Split into Winning 
        winningList=getCardList(line,0)
        
        #Split into Drawn
        drawnList=getCardList(line,1)
        
        
        totalSum+=getNumberOfWins(winningList,drawnList)
    print(totalSum)
        
if __name__ == '__main__':
    linesFromFile=readFile("input.txt")
    getSumOfValues(linesFromFile)