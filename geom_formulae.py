
from numpy import *
from numbers import Number
import math
from math import sqrt
#================= problem 1 ===============================
def circle_perimeter(radius: Number) -> Number:
    """
    calculate the perimeter of a circle given its radius.
    :param radius: the radius of a circle.
    :return: the perimeter(radius units)
    >>> circle_perimeter(3)

    18.84955592153876
    """
    return 2*pi*radius
#=================== end of problem ======================
#=================== problem 2 ============================
def perimeter_triangle(side1,side2,side3 : Number) -> Number:
    """
    calculate the area of any triangle given its three sides side1,side2 and side3.
    :param side1: the first side of the triangle.
    :param side2: the second side of the triangle.
    :param side3: the third side of the triangle.
    :return: the area of the triangle(perimeter = side1+side2+side3)
    >>> perimeter_triangle(3,4,6)
    13
    """
    return side1+side2+side3
print(perimeter_triangle(3,4,6))
#======================== end of problem 2 ===========================
#======================== begining problem 3 ==========================
def area_triangle(a,b,c: Number) -> Number:
    """
    calculate area of any triangle given its three sides.
    :param a: the first side of the triangle.
    :param b: the second side of the triangle.
    :param c: the third side of the triangle.
    :return: the area of the triangle(area = math.sqrt((a+b+c)/2.0)*((a+b+c)/2.0-a)*((a+b+c)/2.0-b)*((a+b+c)/2.0-c)))
    >>> area_triangle(10,2,9)
    20.657360976175056

    """
    return math.sqrt((a+b+c)/2.0)*((a+b+c)/2.0-a)*((a+b+c)/2.0-b)*((a+b+c)/2.0-c)

#========================= end of problem 3 ==============================================
#========================= begining problem 4 ============================================











