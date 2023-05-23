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
    return convertedValue

"""
evaluate the sine of an angle between 0 to pi/4 using the polynomial approximation of sin(x)
parameter: inputted angle value
returns: sine value of the angle
"""
 
def evalSin(convertedValue):
    return sineValue

"""
gets the actual trig value of the inputted angle value, accounting for angle symmetry 
parameter: inputted angle value, sine value of the same angle
returns: a final trig function value
"""
 
def convertAngleFinal(convertedValue, sine, functionChoice):
    return finalValue

"""
evaluate an angle's cosine using its sine
parameter: sine value
returns: cosine value
"""
 
def evalCos(sine):
    return cosValue

"""
evaluate an angle's tangent using its sine
parameter: sine value
returns: tangent value
"""
 
def evalTan(sine):
    return tanValue

print("Choose a function to evaluate: \n1. sin(x) \n2. cos(x) \n3. tan(x)\n\nInput the number of the desired function: ")
angleVal = 0
functionChoice = 0


