import numpy as np
from . import elementwise


def au(x_au, dfdx, y_au, dfdy):
    """
    Estimate the absolute uncertainty of function f(x,y), assuming x and y
    are not correlated.

    Parameters
    ----------
    x_au : float
        Absolute uncertainty of x.
    y_au : float
        Absolute uncertainty of y.
    dfdx : float
        Derivative of f(x,y) w.r.t x, at (x,y).
    dfdy : float
        Derivative of f(x,y) w.r.t x, at (x,y).

    Returns
    -------
    Absolute uncertainty : float
    """
    return np.sqrt((dfdx * x_au) ** 2 + (dfdy * y_au) ** 2)


def add(x, y):
    """
    Add x to y.

    Parameters
    ----------
    x : tubple(float, float)
        Value and absolute uncertainty of x
    y : tubple(float, float)
        Value and absolute uncertainty of y

    Returns
    -------
    x + y and absolute uncertainty : tuple(float, float)

    Derivative
    ----------
    f(x,y) = x + y
    df/dx = 1
    df/dy = 1
    """
    return x[0] + y[0], au(x_au=x[1], dfdx=1.0, y_au=y[1], dfdy=1.0)


def multiply(x, y):
    """
    Multiply x by y.

    Parameters
    ----------
    x : tubple(float, float)
        Value and absolute uncertainty of x
    y : tubple(float, float)
        Value and absolute uncertainty of y

    Returns
    -------
    x * y and abs. uncertainty : tuple(float, float)

    Derivative
    ----------
    f(x,y) = x * y
    df/dx = y
    df/dy = x
    """
    return x[0] * y[0], au(x_au=x[1], dfdx=y[0], y_au=y[1], dfdy=x[0])


def divide(x, y):
    """
    Divide x by y.

    Parameters
    ----------
    x : tubple(float, float)
        Value and absolute uncertainty of x
    y : tubple(float, float)
        Value and absolute uncertainty of y

    Returns
    -------
    x / y and abs. uncertainty : tuple(float, float)

    derivative
    ----------
    f(x,y) = x * y^{-1}
    df/dx = 1
    df/dy = -1x * y^{-2}
    """
    return (
        x[0] / y[0],
        au(x_au=x[1], dfdx=1.0 / y[0], y_au=y[1], dfdy=(-1 * x[0] * y[0] ** (-2))),
    )


def integrate(f, x_bin_edges):
    """
    Integrate function f(x).

    Parameters
    ----------
    f : tuple(array of floats, array of floats)
        Values and absolute uncertainties of f(x)
    x_bin_edges : array of floats
        Edges of bins in x.

    Returns
    -------
    Integral and uncertainty : tuple(float, float)
    """
    f_au = np.array(f[1])
    f = np.array(f[0])
    num_bins = len(x_bin_edges) - 1
    assert len(f) == len(f_au)
    assert len(f) == num_bins

    a = np.zeros(num_bins)
    a_au = np.zeros(num_bins)
    for i in range(num_bins):
        step = x_bin_edges[i + 1] - x_bin_edges[i]
        assert step >= 0.0
        a[i], a_au[i] = multiply(x=(f[i], f_au[i]), y=(step, 0.0))
    return elementwise.add((a, a_au))
