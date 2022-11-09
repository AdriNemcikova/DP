import numpy as np

from elisa import const as c
from elisa.binary_system.model import (
    potential_value_primary,
    potential_value_secondary,
    pre_calculate_for_potential_value_primary,
    pre_calculate_for_potential_value_secondary
)


def correct_sma(mass_ratio, r1, r2):
    """
    Function will provide a values for sma and period that will create binary models with surface g within table
    coverage.

    :param mass_ratio: float;
    :param r1: float;
    :param r2: float;
    :return: tuple; sma in sol rad, period in days
    """
    mid_g = 270
    m1 = 4e30
    m2 = mass_ratio * m1

    sma1 = np.sqrt(c.G * m1 / (r1**2 * mid_g))
    sma2 = np.sqrt(c.G * m2 / (r2**2 * mid_g))

    sma = 0.5 * (sma1 + sma2)
    period = np.sqrt(c.FULL_ARC**2 * sma**3 / (c.G * (m1 + m2)))

    return 1.4374e-9 * sma, period / 86400


def back_radius_potential_primary(radius, mass_ratio, synchronicity=1.0, distance=1.0):
    """
    Returns potential for given side radius.

    :param distance: float;
    :param synchronicity: float;
    :param radius: float;
    :param mass_ratio: float;
    :return: float;
    """
    # (F, q, d, phi, theta)
    args = (synchronicity, mass_ratio, distance, c.PI, c.HALF_PI)
    pot_args = pre_calculate_for_potential_value_primary(*args, return_as_tuple=True)
    return potential_value_primary(radius, mass_ratio, *pot_args)


def back_radius_potential_secondary(radius, mass_ratio, synchronicity=1.0, distance=1.0):
    """
    Returns potential for given side radius.

    :param radius: float; side radius of the secondary component
    :param mass_ratio: float;
    :return: float;
    """
    # (F, q, d, phi, theta)
    args = (synchronicity, mass_ratio, distance, c.PI, c.HALF_PI)
    pot_args = pre_calculate_for_potential_value_secondary(*args, return_as_tuple=True)
    return potential_value_secondary(radius, mass_ratio, *pot_args)

