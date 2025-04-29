
from charge import Charge
import numpy as np
import matplotlib.pyplot as plt


def gradient(values: np.ndarray):
    """
    Compute the gradients of a 2d numpy array. Does not assume
    any number of dimensions. Edges are computed using a 
    forward/backward difference.

    This function will return a list of arrays, one for
    each axis. This is identical to the behavior of numpy's
    gradient function.
    """
    if values.ndim != 2:
        raise ValueError("This gradient function only supports 2-D arrays!")
    # handle the bulk
    g_0 = np.zeros_like(values)
    g_1 = np.zeros_like(values)

    g_0[1:-1] = (values[2:, :] - values[:-2, :]) / 2
    g_1[:, 1:-1] = (values[:, 2:] - values[:, :-2]) / 2

    #handle edges
    g_0[0] = values[1] - values[0]
    g_0[-1] = values[-1] - values[-2]

    g_1[:, 0] = values[:, 1] - values[:, 0]
    g_1[:, -1] = values[:, -1] - values[:, -2]

    return g_0, g_1


if __name__ == "__main__":
    xgrid, ygrid = np.meshgrid(np.linspace(-25, 26), np.linspace(-25, 26))
    charges = [Charge(7.5, 0, 1), Charge(-7.5, 0, -1)]
    potential = np.zeros_like(xgrid)
    for charge in charges:
        potential += charge.potential(xgrid, ygrid)

    grads = gradient(potential)
    np_grads = np.gradient(potential)

    if np.all(grads[0] == np_grads[0]) and np.all(grads[1] == np_grads[1]):
        print("Success! My gradient is identical to numpy's")
    else:
        print(
            "Problem! My gradient function got different results from numpy's")
