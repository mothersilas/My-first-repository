


def area_rhombus(b=None, a=None, d1=None, d2=None, s=None, theta=None):
    """
      calculate the area of a rhombus given different parameters.
    :param b: the length of the base of the rhombus.
    :param a: the heigth of the rhombus.
    :param d1: the length of one diagonal of the rhombus.
    :param d2: the length of the other diagonal of the rhombus.
    :param s:  the length of any side of the rhombus.
    :param theta: is any interior angle of the rhombus.
    :return: the area of a rhombus(area = b*a,d1*d2/2,sin(theta)*s**2)
    """
    if (b=is not None)&(a=is not None):
        area = b*a
        return b*a
    else:
    if (d1=is not None)&(d2=is not None):
        area = d1*d2/2
        return d1*d2/2
    else:
    if (s=is not None)&(theta=is not None):
        area = sin(theta)*s**2
        return sin(theta)*s**2
    else:
        it is imposible to determine the area.
    print(area_rhombus(10,2))









