import re

def part1(sum):
    sum=loopThroughList("input1.txt",sum)
    return sum

def part2(sum):
    sum=loopThroughList2("input1.txt",sum)
    return sum

def listToSingleNumber(intList):
    return (intList[0]*10)+intList[1]

def loopThroughList(fileLocation, addedSum):
    with open(fileLocation, 'r') as fileobj:
        for row in fileobj:
            row=row.rstrip('\n')
            listInts=getintList(row)
            addedSum=addedSum+listToSingleNumber(listInts)
    return addedSum

def loopThroughList2(fileLocation, addedSum):
    with open(fileLocation, 'r') as fileobj:
        for row in fileobj:
            row=row.rstrip('\n')
            listInts=getintList2(row)
            singleNumber=listToSingleNumber(listInts)
            addedSum=addedSum+singleNumber

    return addedSum

def getintList(stringToTest):
    isFirstNumber=True
    numberList=[0,0]
    count=0
    for index,char in enumerate(stringToTest):
        if char.isnumeric():
            if isFirstNumber:
                numberList[0]=int(char)
                count=count+1
                isFirstNumber=False
            else:
                numberList[1]=int(char)
                count=count+1
    if(count==1):
        numberList[1]=numberList[0]
    return numberList

def getintList2(stringToFind):
    
    numberList=[0,0]
    numeric_dict={}
    strNumber_dict={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8, "nine":9 }
    
    #Get the Index of where the ints are and what the value is
    for index,char in enumerate(stringToFind):
        if char.isnumeric():
            numeric_dict[index]=int(char)
    
    #Get were all the word index are and their int value
    for key in strNumber_dict:
        for string in re.finditer(key,stringToFind):
            numeric_dict[string.start()]=strNumber_dict[key]
    
    #Sort the numeric dictionary by index
    numeric_keys=sorted(list(numeric_dict))
    
    #Get the first and last index values    
    numberList[0]=numeric_dict[numeric_keys[0]]
    numberList[1]=numeric_dict[numeric_keys[-1]]
    
    return numberList   


if __name__ == '__main__':
    sum=0
    sum=part1(sum)
    print(sum)
    
    sum=0
    sum=part2(sum)
    print(sum)
