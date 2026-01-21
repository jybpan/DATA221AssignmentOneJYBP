# Question 1:

def consecutiveMultiplication(multThreshold):
    finalProduct = 0
    curNumber = 1

    while finalProduct <= multThreshold:
        finalProduct = curNumber*(curNumber+1)
        curNumber += 1

    print("Final Product: ", finalProduct, "Integer Exceeding Threshold: ", curNumber+1)

consecutiveMultiplication(100)

# Question 2

def nestedDict(strList):
    analyzedDict = None

    for i in strList:
        length = len(i)
        
        if length % 2 == 0:
            parity = "even"
        else:
            parity = "odd"

    #TODO: Turn the calculated things into a nested dict.
    # Turn each value of the list into an empty dictionary, and then iterate through it, 
    # and then update the key with values that correspond to the parity and length.

    return analyzedDict