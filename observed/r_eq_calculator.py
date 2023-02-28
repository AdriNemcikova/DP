"""
    Python skript pre vypocet radiusov
"""

from elisa import BinarySystem


def calculate_requivalent_radii(q, omega1, omega2):
    """
    Calculates equivalent radii of Binary system. (install elisa using: `pip install elisa`)

    :param q: mass ratio M2/M1
    :param omega1: surface potential for primary component
    :param omega2: surface potential for secondary component
    :return: Tuple; ('primary__equivalent_radius', 'secondary__equivalent_radius').
    """
    json_ = {
        "system": {
            "inclination": 90,
            "period": 5.0,
            "argument_of_periastron": 0.0,
            "gamma": 0.0,
            "eccentricity": 0.0,
            "primary_minimum_time": 0.0,
            "phase_shift": 0.0,
            "semi_major_axis": 5.0,
            "mass_ratio": q
        },
        "primary": {
            "surface_potential": omega1,
            "synchronicity": 1.0,
            "t_eff": 8000.0,
            "gravity_darkening": 1.0,
            "albedo": 1.0,
            "metallicity": 0.0
        },
        "secondary": {
            "surface_potential": omega2,
            "synchronicity": 1.0,
            "t_eff": 8000.0,
            "gravity_darkening": 1.0,
            "albedo": 1.0,
            "metallicity": 0.0
        }
    }

    system = BinarySystem.from_json(json_)
    return system.primary.equivalent_radius, system.secondary.equivalent_radius


if __name__ == "__main__":
    print(calculate_requivalent_radii(0.449, 2.98, 2.77))
