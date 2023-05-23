## Aditya Casturi, Henry Zhu, Honors Precalculus, 26 May 2023
## A program to evaluate trignometric functions using the polynomial derivate of sin(x)

import numpy as np
PI = np.pi

"""
converts the inputted angle value to an equivalent value to within the range of 0 to pi/4
parameter: inputted angle value
returns: converted angle value
"""
 
def convertAngle(angleValue):
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
    return convertedValue

"""
evaluate the sine of an angle between 0 to pi/4 using the polynomial approximation of sin(x)
parameter: inputted angle value
returns: sine value of the angle
"""
 
def evalSin(convertedValue):
    sineValue = 0
    return sineValue

"""
gets the actual trig value of the inputted angle value, accounting for angle symmetry 
parameter: inputted angle value, sine value of the same angle
returns: a final trig function value
"""
 
def convertAngleFinal(convertedValue, sine, functionChoice):
    finalValue = 0
    return finalValue

"""
evaluate an angle's cosine using its sine
parameter: sine value
returns: cosine value
"""
 
def evalCos(sine):
    cosValue = 0
    return cosValue

"""
evaluate an angle's tangent using its sine
parameter: sine value
returns: tangent value
"""
 
def evalTan(sine):
    tanValue = 0
    return tanValue

print("Choose a function to evaluate: \n1. sin(x) \n2. cos(x) \n3. tan(x)\n")
functionChoice = int(input("Input the number of the desired function: "))
while functionChoice > 3 or functionChoice < 1 :
    functionChoice = int(input("Invalid input; try again: "))
angleVal = float(input("\nEnter angle value, in radians, to evaluate: "))
print(convertAngle(angleVal))



