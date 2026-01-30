def nestedDict(stringList):
    analyzedDict = {}
    listStats = {}

    for i in stringList:
        length = len(i)

        if(length % 2 == 0):
            parity = "even"
        else:
            parity = "odd"
    
        listStats = {"length":length, "parity":parity}
        analyzedDict[i] = listStats
