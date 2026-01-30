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