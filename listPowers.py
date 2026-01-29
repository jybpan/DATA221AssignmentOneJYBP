def listPairPowerCompute(parameterListPairs):
    parameterListPairPowers = []

    for base, exponent in listPairs:
        if exponent >= 0:
            parameterListPairPowers.append(base**exponent)

    print(parameterListPairPowers)