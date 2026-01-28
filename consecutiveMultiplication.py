finalProduct = 0
currentNumber = 1

while finalProduct <= multThreshold:
    finalProduct = currentNumber*(currentNumber+1)
    currentNumber += 1

print("Final Product: ", finalProduct, "Integer Exceeding Threshold: ", currentNumber+1)