def listWordAnalyzation(parameterList):
    analyzedDictionary = {}
    listStatistics = {}

    for element in parameterList:
        elementLength = len(element)

        if (elementLength % 2 == 0):
            wordParity = "even"
        else:
            wordParity = "odd"
    
        listStatistics = {"length":elementLength, "parity":wordParity}
        analyzedDictionary[i] = listStatistics