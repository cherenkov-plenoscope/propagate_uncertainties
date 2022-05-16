import numpy as np


def au(dfdx, x_au):
    """
    Absolute uncertainty of function f(x0, x1, x2, ...), assuming the
    x are not correlated.

    Parameters
    ----------
    dfdx : array of floats, length N
        Derivatives of f w.r.t. x1 to xN.
    x_au : array of floats, length N
        Absolute uncertainties of x1 to xN.
    Returns
    -------
    Absolute uncertainty : float
    """
    dfdx = np.array(dfdx)
    x_au = np.array(x_au)
    assert len(dfdx) == len(x_au)
    S = 0.0
    for i in range(len(x_au)):
        S += (dfdx[i] * x_au[i]) ** 2.0
    return np.sqrt(S)


def multiply(x, x_au):
    """
    Multilpy all elements in x

    Parameters
    ----------
    x : array of floats
        Values to be multiplied
    x_au : array of floats
        Uncertainties of values x.

    Returns
    -------
    Product and abs. uncertainty : tuple(float, float)
    """
    x = np.array(x)
    x_au = np.array(x_au)
    assert len(x) == len(x_au)
    P = np.prod(x)
    dfdxs = []
    for i in range(len(x)):
        mask_i = np.ones(len(x), dtype=np.bool)
        mask_i[i] = False
        dfdxi = np.prod(x[mask_i])
        dfdxs.append(dfdxi)

    Pau = au(dfdx=dfdxs, x_au=x_au)
    return P, Pau


def add(x, x_au):
    """
    Add all elements in x

    Parameters
    ----------
    x : array of floats
        Values to be added up
    x_au : array of floats
        Uncertainties of values x.

    Returns
    -------
    Sum and abs. uncertainty : tuple(float, float)
    """
    x = np.array(x)
    x_au = np.array(x_au)
    assert len(x) == len(x_au)
    S = np.sum(x)
    dfdxs = np.ones(len(x))
    S_au = au(dfdx=dfdxs, x_au=x_au)
    return S, S_au
