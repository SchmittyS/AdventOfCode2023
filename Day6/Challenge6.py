import re

def readFile(fileLocation):
    lines=[]
    with open(fileLocation, 'r') as fileobj:
        for row in fileobj:
            row=row.rstrip('\n')
            lines.append(row)
    
    return lines

def calcNumWaysToBeatRecord(raceLength, recordDistance):
    numRecordBeaters=0
    for timeHeld in range(raceLength):
        distTraveled=(raceLength-timeHeld)*timeHeld
        if(distTraveled>recordDistance):
            numRecordBeaters+=1
            
    return numRecordBeaters


if __name__ == '__main__':
    linesFromFile=readFile("Input.txt")
    
    timeStr=linesFromFile[0]
    
    timeList = re.findall(r'\d+', timeStr) 
    
    
    distStr=linesFromFile[1]
    distList = re.findall(r'\d+', distStr) 
    
    total=1
    
    #Part 1
    for idx,val in enumerate(timeList):
        raceLength=int(val)
        recordDistance=int(distList[idx])
        total=total*calcNumWaysToBeatRecord(raceLength, recordDistance)
    
    print("Part 1 Solution: "+str(total))
    
    #Part 2
    timeStr=timeStr.replace("Time:","")
    timeStr=timeStr.replace(" ","")
    
    distStr=distStr.replace("Distance:","")
    distStr=distStr.replace(" ","")
    
    raceLength=int(timeStr)
    recordDistance=int(distStr)
    
    partTwoAnswer=calcNumWaysToBeatRecord(raceLength,recordDistance)
    print("Part 1 Solution: "+str(partTwoAnswer))
    
    


