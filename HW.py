#************************  begining of  problem 1 ****************************
#lineplot.py
import numpy as np
from pylab import *
from geom_formulae import *
import pylab as pl

#******************************************************************************
v_square_area = np.vectorize(square_area)
v_square_perimeter = np.vectorize(square_perimeter)

S = np.linspace(0, 10)
A = v_square_area(S)
P = v_square_perimeter(S)

plot(S, A, '-r', label="Area")
plot(S, P, ':b', label="Perimeter")

xlabel('side length')
ylabel('geo values')
title('Square Geo Properties')
legend(loc='upper right')

#show()
#*****************************************   **************************************

#***************************************   *****************************************

v_circle_area = np.vectorize(circle_area)
v_circle_perimeter = np.vectorize(circle_perimeter)

s = np.linspace(5, 10)
A = v_circle_area(s)
P = v_circle_perimeter(s)

plot(s, A, '-r', label="Area")
plot(s, P, ':b', label="Perimeter")

xlabel('side length')
ylabel('geo values')
title('Square Geo Properties')
legend(loc='upper right')

show()













