# Config file with attributes we need to use when calculating light curve

SYSTEM_DICT = {
        'system': {
            'mass_ratio': None,
            'argument_of_periastron': 0.,
            'gamma': 0.,
            'period': 10.0,  # placeholder !!
            'eccentricity': 0.,
            'inclination': None,
            'primary_minimum_time': 0.,
            'semi_major_axis': 10.0  # placeholder !!
        },
        'primary': {
            't_eff': 10000,  # placeholder !!!
            'synchronicity': 1.0,
            'surface_potential': 100,  # placeholder !!

        },
        'secondary': {
            't_eff': 10000,  # placeholder !!!
            'synchronicity': 1.0,
            'surface_potential': 100,  # placeholder !!!
        },
    }

DEFAULT_PASSBAND = 'Generic.Bessell.B'

# bolometric
# Generic.Bessell.U
# Generic.Bessell.B
# Generic.Bessell.V
# Generic.Bessell.R
# Generic.Bessell.I
# SLOAN.SDSS.u
# SLOAN.SDSS.g
# SLOAN.SDSS.r
# SLOAN.SDSS.i
# SLOAN.SDSS.z
# Generic.Stromgren.u
# Generic.Stromgren.v
# Generic.Stromgren.b
# Generic.Stromgren.y
# Kepler
# GaiaDR2
# TESS
