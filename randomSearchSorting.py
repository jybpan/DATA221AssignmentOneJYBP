def sortedSearch():
    from random import random

    values = [random() for i in range(20)]
    x = random()

    firstMatchingIndex = 0
    counter = 0
    sortedRandomList = sorted(randomValues)

    finalListIndex = len(sortedRandomList)-1

    for index in range(finalListIndex):
        if sortedRandomList[index] >= x and counter == 0:
            firstMatchingIndex = i
            counter += 1