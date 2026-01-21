# Question 1:

def consecutiveMultiplication(multThreshold):
    finalProduct = 0
    curNumber = 1

    while finalProduct <= multThreshold:
        finalProduct = curNumber*(curNumber+1)
        curNumber += 1

    print("Final Product: ", finalProduct, "Integer Exceeding Threshold: ", curNumber+1)

consecutiveMultiplication(100)