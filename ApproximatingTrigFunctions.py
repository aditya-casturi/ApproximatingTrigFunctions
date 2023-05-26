# Aditya Casturi, Henry Zhu, Honors Precalculus, 26 May 2023
# A program to evaluate trignometric functions using the polynomial derivate of sin(x)

from numpy import pi as PI

def fitAngleToRange(angle):
    """
    Maps an angle value to an equivalent angle value within the range of 0 to PI/4.

    Args:
        angle (float): The angle value to be mapped.

    Returns:
        float: The equivalent angle value within the range of 0 to PI/4.
    """
    angle = angle % (2 * PI)
    if 0 <= angle <= PI / 4:
        return angle
    if PI / 4 < angle <= PI / 2:
        return PI / 2 - angle
    if PI / 2 < angle <= 3 * PI / 4:
        return angle - PI / 2
    if 3 * PI / 4 < angle <= PI:
        return PI - angle
    if PI < angle <= 5 * PI / 4:
        return angle - PI
    if 5 * PI / 4 < angle <= 3 * PI / 2:
        return 3 * PI / 2 - angle
    if 3 * PI / 2 < angle <= 7 * PI / 4:
        return angle - 3 * PI / 2
    if 7 * PI / 4 < angle <= 2 * PI:
        return 2 * PI - angle


def adjustSine(angle, sinValue):
    """
    Maps a sine value back to the original sine value before it was transformed by the fitAngleToRange function.

    Args:
        angle (float): The original angle value before it was transformed by the fitAngleToRange function.
        sinValue (float): The sine value to be mapped back to the original sine value.

    Returns:
        float: The original sine value before it was transformed by the fitAngleToRange function.
    """
    theta = angle % (2 * PI)
    if 0 <= theta <= PI / 4:
        return sinValue
    if PI / 4 < theta <= PI / 2:
        return cos(angle, sinValue)
    if PI / 2 < theta <= 3 * PI / 4:
        return -cos(angle, sinValue)
    if 3 * PI / 4 < theta <= PI:
        return sinValue
    if PI < theta <= 5 * PI / 4:
        return -sinValue
    if 5 * PI / 4 < theta <= 3 * PI / 2:
        return cos(angle, sinValue)
    if 3 * PI / 2 < theta <= 7 * PI / 4:
        return -cos(angle, sinValue)
    if 7 * PI / 4 < theta <= 2 * PI:
        return -sinValue


def sin(angle):
    """
    Calculates the sine of an angle value using a polynomial expression.

    Args:
        angle (float): The angle value in radians.

    Returns:
        float: The sine of the angle value.
    """
    inputAngle = fitAngleToRange(angle)
    assert inputAngle is not None
    result = 0

    for n in range(15):
        term = (-1) ** n
        term *= inputAngle ** (1 + 2 * n)
        term /= factorial(1 + 2 * n)
        result += term

    return adjustSine(angle, result)


def cos(angle, sinValue):
    """
    Calculates the cosine of an angle value using the sine value and the quadrant of the angle.

    Args:
        angle (float): The angle value in radians.
        sinValue (float): The sine of the angle value.

    Returns:
        float: The cosine of the angle value.
    """
    angle = angle % (2 * PI)

    if PI / 2 < angle < 3 * PI / 2:
        cos = -(1 - sinValue ** 2) ** (1 / 2)
    else:
        cos = (1 - sinValue ** 2) ** (1 / 2)

    return cos


def tan(angle):
    """
    Calculates the tangent of an angle value using the sine and cosine functions.

    Args:
        angle (float): The angle value in radians.

    Returns:
        float: The tangent of the angle value.
    """
    return sin(angle) / cos(angle, sin(angle))


def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n (int): The non-negative integer to calculate the factorial of.

    Returns:
        int: The factorial of the input integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def evaluateAndPrintOutput(angle, functionChoice):
    """
    Evaluates the trigonometric function specified by the input `functionChoice` for the given `angle`, and prints the result.

    Args:
        angle (float): The angle value in radians.
        functionChoice (int): The integer value representing the trigonometric function to evaluate. 
                              1 for sine, 2 for cosine, 3 for tangent.

    Returns:
        None
    """
    if (functionChoice == 1):
        print("\nsin(x) = ", sin(angle))
    elif (functionChoice == 2):
        print("\ncos(x) = ", cos(angle, sin(angle)))
    else:
        if round(cos(angle,sin(angle)),5) == 0:
            print("\ntan(x) = undefined")
        else:
            print("\ntan(x) = ", tan(angle))


def main():
    """
    Prompts the user to enter an angle value and a trigonometric function choice, 
    and evaluates and prints the result of the selected function for the given angle.
    
    Args:
        None

    Returns:
        None
    """
    print("This program finds the values of trigonometric functions. \n1. sin(x) \n2. cos(x) \n3. tan(x)\n")

    functionChoice = int(input("Enter the number of the function you want to evaluate: "))
    while functionChoice > 3 or functionChoice < 1:
        functionChoice = int(input("Invalid input; try again: "))
    angle = float(input("\nEnter the angle x in radians: "))

    evaluateAndPrintOutput(angle, functionChoice)
    print("\n\n")


if __name__ == "__main__":
    main()