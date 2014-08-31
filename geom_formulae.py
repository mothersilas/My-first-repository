
from numpy import *
from numbers import Number
import math


def volume_ellipsoid(a, b, c: Number) -> Number:
    """
    Find the volume any ellipsoid with all its axises are given.
    @param a: the length on the x-axis.
    @param b: the length on the y-axis.
    @param c: the length on the z-axis.
    @return: the volume of the ellipsoid(volume = 4*pi*a*b*c/3)
    >>> volume_ellipsoid(21, 15, 2)

    2638.9378290154264

    """
    volume = 4*pi*a*b*c/3
    return volume
#print(volume_ellipsoid(21, 15, 2))


def circle_perimeter(radius: Number) -> Number:
    """
    Calculate the perimeter of a circle given its radius.

    @param radius: the radius of a circle.
    @return: the perimeter(radius units)
    >>> circle_perimeter(3)
    18.84955592153876
    """
    perimeter = 2*pi*radius
    return perimeter
#print(circle_perimeter(3))


def perimeter_triangle(side1, side2, side3: Number) -> Number:
    """
    Calculate the area of any triangle given its three sides side1,side2 and side3.

    @param side1: the first side of the triangle.
    @param side2: the second side of the triangle.
    @param side3: the third side of the triangle.
    @return: the area of the triangle(perimeter = side1+side2+side3)
    >>> perimeter_triangle(3, 4, 6)
    13
    """
    perimeter = side1+side2+side3
    return perimeter
#print(perimeter_triangle(3, 4, 6))


def area_triangle(a, b, c: Number) -> Number:
    """
    Calculate area of any triangle given its three sides.

    @param a: the first side of the triangle.
    @param b: the second side of the triangle.
    @param c: the third side of the triangle.
    @return: the area of the triangle(area = math.sqrt((a+b+c)/2.0*(b+c-a)/2.0*(a+c-b)/2.0*(a+b-c)/2.0))
    >>> area_triangle(10, 2, 9)
    8.181534085976786
    """
    area = math.sqrt((a+b+c)/2.0*(b+c-a)/2.0*(a+c-b)/2.0*(a+b-c)/2.0)
    return area
#print(area_triangle(10, 2, 9))


def area_regular_polygon(n, s, r: Number) -> Number:
    """
    Calculate the area of a regular polygon given the information number of sides,side length and apothem.

    @param n: the number of sides of a regular polygon.
    @param s: the length of one side of the polygon.
    @param r: the apothem(the radius of the inscribed circle)
    @return: the area of the n sided regular polygon(area = n*s*r/2.0)
    >>> area_regular_polygon(12, 6, 2)
    72
    """
    area = n*s*r/2.0
    return area
#print(area_regular_polygon(12, 6, 2))


def volume_sphere(r: Number) -> Number:
    """
    Find volume of a sphere given its radius.

    @param r: the radius of the sphere.
    @return: the volume of the sphere(volume = 4*pi*r**3/3)
    >>> volume_sphere(10)
      4188.790204786391
    """
    volume = 4*pi*r**3/3
    return volume
#print(volume_sphere(10))


def volume_pyramid(base_area, heigth: Number) -> Number:
    """
    Calculate the volume of a pyramid with base area and heigth given.

    @param base_area: the base area of the pyramid.
    @param heigth: the heigth of the pyramid.
    @return: the volume of the pyramid(volume = basearea*heigth/3)
    >>> volume_pyramid(4,8)
    10.666666666666666

    """
    volume = base_area*heigth/3
    return volume
#print(volume_pyramid(4,8))


def lateral_area_prism(p, h: Number) -> Number:
    """
    Calculate the lateral area of a prism given its perimeter and heigth.

    @param p: the perimeter of the prism.
    @param h: the heigth of the prism
    @return: the lateral area of the prism(area = p*h)
    >>> lateral_area_prism(10, 5)
     50
    """
    lateral_area = p*h
    return lateral_area
#print(lateral_area_prism(10, 5))


def volume_cube(l, w, h: Number) -> Number:
    """
    Find the volume of a cube given all its dimensions.

    @param l: the length of the cube.
    @param w: the width of the cube.
    @param h: the heigth of the cube.
    @return: the volume the cube(volume = l*w*h)
    >>> volume_cube(4, 5, 6)
    120
    """
    volume = l*w*h
    return volume
#print(volume_cube(4, 5, 6))


def volume_frustum_cone(r1, r, h: Number) -> Number:
    """
    Calculate the volume of the frustum of a cone given the three parameters.

    @param r1: radius of the lower base.
    @param r: radius of the upper  base.
    @param h: heigth of the frustum.
    @return: the volume of the frustum(volume = pi*h*(R**2+R*r+r**2)/3)
    >>>volume_frustum_cone(4, 2, 10)
    293.21531433504737
    """
    volume = pi*h*(r1**2+r1*r+r**2)/3
    return volume
#print(volume_frustum_cone(4, 2, 10))


def area_rhom(b, a: Number) ->Number:
    """
    Calculate the area of a rhombus given its base length and heigth.

    @param b: the base length of the rhombus.
    @param a: the heigth of the rhombus.
    @return: the area of the rhombus(area = b*a)
    >>> area_rhom(10, 2)
    20
    """
    area = b*a
    return area
#print(area_rhom(10, 2))


def area_rhombus(s, theta) -> Number:
    """
    Calculate the area of a rhombus given one side and interior angle.

    @param s: the length a side.
    @param theta: interior angle of the triangle.
    @return: the area of the rhombus( area = sin(theta)*s**2)
    >>> area_rhombus(2, pi/2)
      4
    """
    area = sin(theta)*(s**2)
    return area
#print(area_rhombus(2, pi/2))


def area_rhomb(b=None, a=None, d1=None, d2=None, s=None, theta=None):
    """
    Calculate the area of a rhombus given different parameters.

    @param b: the length of the base of the rhombus.
    @param a: the heigth of the rhombus.
    @param d1: the length of one diagonal of the rhombus.
    @param d2: the length of the other diagonal of the rhombus.
    @return: the area of a rhombus(area = b*a,d1*d2/2,sin(theta)*s**2)
    >>> area_rhomb(b=4, a=7)
    28
    >>> area_rhomb(d1=3, d2=4)
    6
    >>> area_rhomb(s=2, theta=pi/2)
    4
    """
    if (b is not None) & (a is not None):
        area = b*a
        return area
    elif (d1 is not None) & (d2 is not None):
        area = (d1*d2)/2
        return area
    else:
        area = (s**2)*sin(theta)
        return area
#print(area_rhomb(b=4, a=7,d1=None, d2=None, s=None, theta=None ))
#print(area_rhomb(b=None, a=None, d1=3, d2=4, s=None, theta=None))
#print(area_rhomb(b=None, a=None, d1=None, d2=None, s=2, theta=pi/2))


def distance_points_2d(x1, y1, x2, y2):
    """
    Find the distance between two given points in 2D.

    @param x1: the first coordinate of the first point.
    @param x2: the first coordinate of the second point.
    @param y1: the second coordinate of the first point.
    @param y2: the second coordinate of the second point.
    @return: the distance between two points(same units).
    >>> distance_points_2d(0, 0, 4, 0)
     4
    """
    d1 = (x2-x1)*(x2-x1)
    d2 = (y2-y1)*(y2-y1)
    distance = math.sqrt(d1+d2)
    return distance
#print(distance_points_2d(0, 0, 4, 0))
#print(distance_points_2d(4, 10, 2, 3))


def distance_points_3d(x1, y1, z1, x2, y2, z2):
    """
    Find the distance between two given points in 3D.

    @param x1: the first coordinate of the first point.
    @param y1: the second coordinate of the first point.
    @param z1: the third coordinate of the first point.
    @param x2: the first coordinate of the second point.
    @param y2: the second coordinate of the second point.
    @param z2: the third coordinate of the second point.
    @return: the distance between two points(same units).
    >>> distance_points_3d(0, 0, 0, 6, 0, 0)
     6
    """
    d1 = (x2-x1)*(x2-x1)
    d2 = (y2-y1)*(y2-y1)
    d3 = (z2-z1)*(z2-z1)
    distance = math.sqrt(d1+d2+d3)
    return distance
#print(distance_points_3d(0, 0, 0, 6, 0, 0))
#print(distance_points_3d(2, 0, 5, 4, 0, 0))
