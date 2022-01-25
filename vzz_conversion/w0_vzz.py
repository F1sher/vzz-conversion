import numpy as np


e = 1.602e-19
hbar = 1.055e-34 

def vzz_to_w0(vzz: float, eta:float, Q:float) -> float:
    """
    Calculate w0 frequency from given Vzz, \eta and Q for I = 5/2 (111Cd, 181Ta, etc.).

    Parameters
    ----------
    vzz -- EFG value in [V/m^2]
    eta -- Asymmetry parameter value
    Q -- Nuclear electric quadrupole moment value in [m^2]

    Returns
    ----------
    frequency value in [1/s]
    """
    beta = 80.0 * (1.0 - eta**2) / (28/3 * (3.0 + eta**2))**1.5
    w0 = (e * Q * vzz * (7 * (3 + eta**2))**0.5 *
          np.sin(np.arccos(beta) / 3) / (10 * hbar))

    return w0

def w0_to_vzz(w0: float, eta:float, Q:float) -> float:
    """
    Calculate Vzz from given w0 (exp. frequency), \eta and Q for I = 5/2 (111Cd, 181Ta, etc.).
    """
    beta = 80.0 * (1.0 - eta**2) / (28/3 * (3.0 + eta**2))**1.5
    vzz = (10 * hbar * w0 /
           (e * Q * (7 * (3 + eta**2))**0.5 * np.sin(np.arccos(beta) / 3) ))

    return vzz
