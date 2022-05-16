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


def add(x, x_au, y, y_au):
    """
    Add x to y.

    Parameters
    ----------
    x : float
        Value x.
    x_au : float
        Absolute uncertainty of x.
    y : float
        Value y.
    y_au : float
        Absolute uncertainty of y.

    Returns
    -------
    x + y and abs. uncertainty : tuple(float, float)

    derivative
    ----------
    f(x,y) = x + y
    df/dx = 1
    df/dy = 1
    """
    return x + y, au(x_au=x_au, dfdx=1.0, y_au=y_au, dfdy=1.0)


def multiply(x, x_au, y, y_au):
    """
    Multiply x by y.

    Parameters
    ----------
    x : float
        Value x.
    x_au : float
        Absolute uncertainty of x.
    y : float
        Value y.
    y_au : float
        Absolute uncertainty of y.

    Returns
    -------
    x * y and abs. uncertainty : tuple(float, float)

    derivative
    ----------
    f(x,y) = x * y
    df/dx = y
    df/dy = x
    """
    return x * y, au(x_au=x_au, dfdx=y, y_au=y_au, dfdy=x)


def divide(x, x_au, y, y_au):
    """
    Divide x by y.

    Parameters
    ----------
    x : float
        Value x.
    x_au : float
        Absolute uncertainty of x.
    y : float
        Value y.
    y_au : float
        Absolute uncertainty of y.

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
        x / y,
        au(x_au=x_au, dfdx=1.0 / y, y_au=y_au, dfdy=(-1 * x * y ** (-2))),
    )


def integrate(f, f_au, x_bin_edges):
    """
    Integrate function f(x).

    Parameters
    ----------
    f : array of floats
        Values of function f(x).
    f_au : array of floats
        Absolute uncertainty of function f(x).
    x_bin_edges : array of floats
        Edges of bins in x.

    Returns
    -------
    Integral and uncertainty : tuple(float, float)
    """
    num_bins = len(x_bin_edges) - 1
    assert len(f) == len(f_au)
    assert len(f) == num_bins

    a = np.zeros(num_bins)
    a_au = np.zeros(num_bins)
    for i in range(num_bins):
        step = x_bin_edges[i + 1] - x_bin_edges[i]
        assert step >= 0.0
        a[i], a_au[i] = multiply(x=f[i], x_au=f_au[i], y=step, y_au=0.0)
    return elementwise.add(x=a, x_au=a_au)
