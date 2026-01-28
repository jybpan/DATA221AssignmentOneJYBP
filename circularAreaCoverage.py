def circleAreaCoverage(circleOneRadii, circleTwoRadii):
    import math
    pi = math.pi

    if circleOneRadii < 0 or circleTwoRadii < 0 :
        return "One of the radii you have given is invalid (i.e smaller than 0)."

    circleOneRadiusSqrd = circleOneRadii**2
    circleOneArea = pi*circleOneRadiusSqrd

    circleTwoRadiusSqrd = circleTwoRadii**2
    circleTwoArea = pi*circleTwoRadiusSqrd

    largestCircle = max(circleOneArea, circleTwoArea)
    smallestCircle = min(circleOneArea, circleTwoArea)

    percentileAreaCoverage = float(smallestCircle/largestCircle)*100
    
    return format(percentileAreaCoverage, ".2f")