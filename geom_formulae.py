
from numpy import *
from numbers import Number
import math
from math import sqrt
#======================= problem 1 ============================
def volume_ellipsoid(a,b,c: Number) -> Number:
    """
    find the volume any ellipsoid with all its axises are given.
    @param a: the length on the x-axis.
    @param b: the length on the y-axis.
    @param c: the length on the z-axis.
    @return: the volume of the ellipsoid(volume = 4*pi*a*b*c/3)
    >>> volume_ellipsoid(21,15,2)
    2638.9378290154264
    """
    return 4*pi*a*b*c/3

#======================== end of problem 1 ======================

#================= problem 2 ===============================
def circle_perimeter(radius: Number) -> Number:
    """
    calculate the perimeter of a circle given its radius.
    :param radius: the radius of a circle.
    :return: the perimeter(radius units)
    >>> circle_perimeter(3)

    18.84955592153876
    """
    return 2*pi*radius
#=================== end of problem 2 ======================

#=================== problem 3 ============================
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
#======================== end of problem 3 ===========================


#======================== begining problem 4 ==========================

def area_triangle(a,b,c: Number) -> Number:
    """
    calculate area of any triangle given its three sides.
    :param a: the first side of the triangle.
    :param b: the second side of the triangle.
    :param c: the third side of the triangle.
    :return: the area of the triangle(area = math.sqrt((a+b+c)/2.0*(b+c-a)/2.0*(a+c-b)/2.0*(a+b-c)/2.0))
    >>> area_triangle(10,2,9)
    8.181534085976786
    """
    return math.sqrt((a+b+c)/2.0*(b+c-a)/2.0*(a+c-b)/2.0*(a+b-c)/2.0)

 #========================= end of problem 4 ==============================================

 #========================= begining problem 5 ============================================


def area_regularpolygon(n,s,r: Number) -> Number:
    """
    calculate the area of a regular polygon given the information number of sides,side length and apothem.
    :param n: the number of sides of a regular polygon.
    :param s: the length of one side of the polygon.
    :param r: the apothem(the radius of the inscribed circle)
    :return: the area of the n sided regular polygon(area = n*s*r/2.0)
    >>> area_regularpolygon(12,6,2)
    72
    """
    return n*s*r/2.0

#================================= end of problem 5 ===========================================

#================================= begining of problem 6 ==================================
def volume_sphere(r: Number) -> Number:
    """
    Find volume of a sphere given its radius.
    :param r: the radius of the sphere.
    :return: the volume of the sphere(volume = 4*pi*r**3/3)
    >>> volume_sphere(10)
      4188.790204786391
    """
    return 4*pi*r**3/3

#============================== end of problem 6 ===========================================

#============================= begining of problem 7 =======================================

def volume_Pyramid(basearea,heigth: Number) -> Number:
    """
    calculate the volume of a pyramid with base area and heigth given.
    @param basearea: the base area of the payramid.
    @param heigth: the heigth of the pyramid.
    @return: the volume of the pyramid(volume = basearea*heigth/3)
    >>> volume_pyramid(4,8)
    10.666666666666666

    """
    return basearea*heigth/3
#================================ end of problem 7 =========================================

#=============================== begining of problem 8 =====================================

def lateralarea_prism(p,h: Number) -> Number:
    """
    calculate the lateral area of a prism given its perimeter and heigth.
    @param p: the perimeter of the prism.
    @param h: the heigth of the prism
    @return: the lateral area of the prism(area = p*h)
    >>> lateralarea_prism(10,5)
     50
    """
    return p*h
#================================== end of problem 8 =====================================

#================================== begining of problem 9 =================================
def volume_cube(l,w,h: Number) -> Number:
    """
    find the volume of a cube given all its dimensions.
    @param l: the length of the cube.
    @param w: the width of the cube.
    @param h: the heigth of the cube.
    @return: the volume the cube(volume = l*w*h)
    >>> volume_cube(4,5,6)
    120
    """
    return l*w*h
#============================= end of problem 9 =============================================
#================================== begining of problem 10 =====================================

def volume_frustumcone(R,r,h: Number) -> Number:
    """
    calculate the volume of the frustum of a cone given the three parameters.

    @param R: radius of the lower base.
    @param r: radius of the upper  base.
    @param h: heigth of the frustum.
    @return: the volume of the frustum(volume = pi*h*(R**2+R*r+r**2)/3)
    >>>volume_frustumcone(4,2,10)
    293.21531433504737

    """
    return pi*h*(R**2+R*r+r**2)/3
#================================== end of problem 10 ==========================================









