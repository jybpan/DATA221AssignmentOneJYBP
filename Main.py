# Question 1:

def consecutiveMultiplication(multThreshold):
    finalProduct = 0
    curNumber = 1

    while finalProduct <= multThreshold:
        finalProduct = curNumber*(curNumber+1)
        curNumber += 1

    print("Final Product: ", finalProduct, "Integer Exceeding Threshold: ", curNumber+1)

# Question 2

def nestedDict(strList):
    analyzedDict = {}
    listStats = {}

    for i in strList:
        length = len(i)

        if(length % 2 == 0):
            parity = "even"
        else:
            parity = "odd"

        listStats = {"Length":length, "Parity":parity}

    print(listStats)
    print(analyzedDict)

test = ["Data", "Science"]

nestedDict(test)