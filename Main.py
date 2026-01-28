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
    
        listStats = {"length":length, "parity":parity}
        analyzedDict[i] = listStats

    print(listStats)
    print(analyzedDict)

# Question 3

def safeFunction(listPairs):
    listPowers = []

    for base, exponent in listPairs:
        if exponent >= 0:
            listPowers.append(base**exponent)

    print(listPowers)

# Question 4

def sortedSearch():
    from random import random

    values = [random() for i in range(20)]
    x = random()

    firstMatchingIdx = 0
    counter = 0
    sortedList = sorted(values)

    finalIndex = len(sortedList)-1

    for i in range(finalIndex):
        if sortedList[i] >= x and counter == 0:
            firstMatchingIdx = i
            counter += 1
    
    print(sortedList, x, firstMatchingIdx)

# Question 5

def circleAreaCoverage(circleOneRadii, circleTwoRadii):
    import math
    pi = math.pi

    if circleOneRadii < 0 or circleTwoRadii < 0 :
        return "One of the radii you have given is invalid (i.e smaller than 0)."

    circleOneRadiusSqrd = circleOneRadii**2
    circleOneArea = pi*circleOneRadiusSqrd

    circleTwoRadiusSqrd = circleTwoRadii**2
    circleTwoArea = pi*circleTwoRadiusSqrd

    largestCircle = max(circleOneArea, circleTwoArea)
    smallestCircle = min(circleOneArea, circleTwoArea)

    percentileAreaCoverage = float(smallestCircle/largestCircle)*100
    
    return format(percentileAreaCoverage, ".2f")

# Question 6

def distributionAnalysis(numbersList):
    keyPercentageDict = {k: None for k in numbersList}
    keySortedDict = {}
    count = 0

    print(keyPercentageDict)
    print(keyPercentageDict.keys())

    for i in keyPercentageDict.keys():
        for j in keyPercentageDict.keys():
            if i >= j:
                count += 1
                print("Count: ",count)
        numPercentile = count/len(keyPercentageDict)
        print("Percentage: ", numPercentile)
        keyPercentageDict[i] = numPercentile
        count = 0

    for k in sorted(keyPercentageDict.keys()):
        keySortedDict[k] = keyPercentageDict[k]

    return keySortedDict

# Question 7

def timeConversion():
    userTimeInput = int(input("Give time in seconds since midnight to be converted. "))

    seconds = userTimeInput
    minutes = seconds/60
    hours = minutes/60 
    meridianTime = ""

    if hours > 12:
        meridianTime = "PM"
    else:
        meridianTime = "AM"

    return(f"\nIt has been {seconds} seconds since Midnight, or:\n{round(minutes, 4)} Minutes\n{round(hours, 4)} Hours\nAnd it is in the {meridianTime}.")

def dataframeExtrapolation():
    import pandas as pd

    data = {
        "A": [1, 2, 2, 1],
        "B": [3.1, 4.2, 1.5, 6.3],
        "C": [800, 150, 400, 210]
    }

    df = pd.DataFrame(data=data)
    df['mean'] = df.mean(axis=1)


    