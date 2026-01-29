product = 1
currentNumber = 1
multiplierThreshold = 100

while product <= multiplierThreshold:
    product = currentNumber*(currentNumber+1)
    currentNumber += 1

print("Final Product: ", product, "Integer Exceeding Threshold: ", currentNumber+1)