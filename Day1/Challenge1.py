testString0 = "1aaaa3"
testString1="ssd3esdsa34"


def part1(sum):
    sum=loopThroughList("input1.txt",sum)
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

if __name__ == '__main__':
    sum=0
    sum=part1(sum)
    print(sum)
