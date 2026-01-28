def safeFunction(listPairs):
    listPowers = []

    for base, exponent in listPairs:
        if exponent >= 0:
            listPowers.append(base**exponent)

    print(listPowers)