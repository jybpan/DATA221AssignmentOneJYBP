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