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