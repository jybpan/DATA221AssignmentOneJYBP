def distributionAnalysis(numbersList):
    parsedDictionary = {k: None for k in numbersList}
    keySortedDictionary = {}
    count = 0

    parsedDictionaryKeys = parsedDictionary.keys()

    for comparedElementOne in parsedDictionaryKeys:
        for comparedElementTwo in parsedDictionaryKeys:
            if comparedElementOne >= comparedElementTwo:
                count += 1

        numericPercentile = count/len(parsedDictionary)
        parsedDictionary[i] = numericPercentile

        count = 0 # Reset the Count

    for key in sorted(parsedDictionaryKeys):
        keySortedDictionary[key] = parsedDictionary[key]

    return keySortedDictionary