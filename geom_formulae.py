# ===============Geometry ================================
from numbers import Number

def square_perimeter(side : Number) -> Number:
    """
    calculate perimeter of a square from side length.
    :param side: the side length
    :return: the perimeter (same unit as side length)
    >>> square_perimeter(4)
    16
    """

    return 4*side



def square_area(side):
    """
    calculate area of a square from side length.
    :param side: the side length
    :return: the area (units^2 from side)
    >>> square_area(4)
    16
    """
    return side*side
if __name__ =="_main_":
    sampleSide = 4
    print("area:",
          square_area(sampleSide),
             "perimeter:",
   square_perimeter(sampleSide))

print(square_area(2))
print(square_perimeter(5))
print(square_perimeter(1))



# =====================End==========================================

