from math import sqrt

def hyperbola(x):
    assert abs(x) > 1.
    return sqrt(x**2 - 1)
