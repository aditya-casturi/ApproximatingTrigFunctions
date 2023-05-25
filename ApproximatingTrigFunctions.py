# Aditya Casturi, Henry Zhu, Honors Precalculus, 26 May 2023
# A program to evaluate trignometric functions using the polynomial derivate of sin(x)

import numpy as np
PI = np.pi

"""
converts the inputted angle value to an equivalent value to within the range of 0 to pi/4
parameter: inputted angle value
returns: converted angle value
"""


def convertAngle(angleValue):
    convertedValue = 0
    while angleValue >= 2*PI:
        convertedValue = angleValue-(2*PI)
        if convertedValue < 2*PI:
            break
    while angleValue < 0:
        convertedValue = angleValue+(2*PI)
        if convertedValue > 0:
            break
    if angleValue >= 0 and angleValue < PI/4:
        convertedValue = angleValue
    if angleValue > PI/4 and angleValue <= PI/2:
        convertedValue = PI/2 - angleValue
    if angleValue > PI/2 and angleValue <= (3*PI)/4:
        convertedValue = angleValue - PI/2
    if angleValue > (3*PI)/4 and angleValue <= PI:
        convertedValue = PI - angleValue
    if angleValue > PI and angleValue <= (5*PI)/4:
        convertedValue = angleValue - PI
    if angleValue > (5*PI)/4 and angleValue <= (3*PI)/2:
        convertedValue = angleValue - (3*PI)/2
    if angleValue > (3*PI)/2 and angleValue <= (7*PI)/4:
        convertedValue = (3*PI)/2 - angleValue 
    if angleValue > (7*PI)/4 and angleValue < 2*PI:
        convertedValue = 2*PI - angleValue

    return angleValue


"""
evaluate the sine of an angle between 0 to pi/4 using the polynomial approximation of sin(x)
parameter: converted angle value
returns: sine value of the angle
"""


def evalSin(value):
    result = 0

    for n in range(15):
        term = (-1) ** n
        term *= value ** (2*n + 1)
        term /= factorial(2*n + 1)
        result += term

    return result


"""
evaluates and prints the actual trig value of the inputted angle value, accounting for angle symmetry
parameters: converted angle value, function choice
returns: appropriate trig value of the angle
"""


def evaluateTrigValue(angleVal, functionChoice):
    sine = evalSin(angleVal)

    if functionChoice == 1:
        return sine
    elif functionChoice == 2:
        return evalCos(sine)
    elif functionChoice == 3:
        return evalTan(sine)


"""
evaluate an angle's cosine using its sine
parameter: sine value
returns: cosine value
"""


def evalCos(sine):
    # Pythagorean identity: cos(x) = √(1 - sin(x)^2)
    cosValue = (1 - sine ** 2) ** 0.5
    return cosValue


"""
evaluate an angle's tangent using its sine
parameters: sine value, converted angle value
returns: tangent value
"""


def evalTan(sine):
    # tan(x) = sin(x) / cos(x)
    cosValue = evalCos(sine)
    tanValue = sine / cosValue
    return tanValue


"""
evaluate the factorial of a number
parameter: inputted number
returns: factorial of the number
"""


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


print("This program finds the values of trigonometric functions. \n1. sin(x) \n2. cos(x) \n3. tan(x)\n")
functionChoice = int(
    input("Enter the number of the function you want to evaluate: "))
while functionChoice > 3 or functionChoice < 1:
    functionChoice = int(input("Invalid input; try again: "))

originalAngleVal = float(input("\nEnter the angle x in radians: "))
convertedAngleVal = convertAngle(originalAngleVal)
trigVal = evaluateTrigValue(convertedAngleVal, functionChoice)

if functionChoice == 1:
    print("sin(", originalAngleVal, ") = ", trigVal, sep="")
elif functionChoice == 2:
    print("cos(", originalAngleVal, ") = ", trigVal, sep="")
elif functionChoice == 3:
    print("tan(", originalAngleVal, ") = ", trigVal, sep="")
