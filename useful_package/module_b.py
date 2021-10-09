import numpy as np

def hyperbola(x):
    assert np.abs(x) > 1.
    return np.sqrt(x**2 - 1)
