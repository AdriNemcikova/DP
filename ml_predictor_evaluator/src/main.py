"""
    A script that is used to plot the actual curve and its corresponding prediction and calculate residuals.
    Data is obtained from files whose path is defined in the main function.
    Plots are saved in defined directories.
"""

import numpy as np
import pandas as pd
import traceback
from copy import copy
from src.eb_gridmaker_fns import correct_sma, back_radius_potential_primary, back_radius_potential_secondary
from operator import xor
from elisa import BinarySystem, Observer
from elisa.analytics.binary_fit.shared import r_squared
from src.config import SYSTEM_DICT, DEFAULT_PASSBAND
from matplotlib import gridspec
import matplotlib.pyplot as plt
import os


def evaluate_parameter_set(parameters, reference_teff, passband, phases):
    q = parameters['mass_ratio']
    i = parameters['inclination']
    t1_to_t2 = parameters['t1_to_t2']
    omega1 = parameters['omega1']
    omega2 = parameters['omega2']
    # r1 = parameters['r1']
    # r2 = parameters['r2']
    r1 = parameters.get('r1', None)
    r2 = parameters.get('r2', None)

    # making sure that either potentials or radii are used, not both at the same time
    if not xor(r1 is None, omega1 is None) or not xor(r2 is None, omega2 is None):
        raise ValueError('Supply either radii (`r1`, `r2`) or surface potentials (`omega1`, `omega2`).')

    system_dict = copy(SYSTEM_DICT)
    system_dict['system']['mass_ratio'] = q
    system_dict['system']['inclination'] = f'{i} rad'

    if r1 is None:
        system_dict['primary']['surface_potential'] = omega1
        system_dict['secondary']['surface_potential'] = omega2
        test_binary = BinarySystem.from_json(system_dict)
        sma, period = correct_sma(q, test_binary.primary.equivalent_radius, test_binary.secondary.equivalent_radius)
    else:
        system_dict['primary']['surface_potential'] = back_radius_potential_primary(r1, q)
        system_dict['secondary']['surface_potential'] = back_radius_potential_secondary(r2, q)

        sma, period = correct_sma(q, r1, r2)
    system_dict['system']['semi_major_axis'] = f"{sma} solRad"
    system_dict['system']['period'] = period

    test_binary = BinarySystem.from_json(system_dict)
    # setting the temperatures
    if reference_teff is None:
        reference_teff = 5500 if test_binary.morphology == 'over-contact' else 10000
    system_dict['primary']['t_eff'] = reference_teff if t1_to_t2 >= 1.0 else reference_teff * t1_to_t2
    system_dict['secondary']['t_eff'] = reference_teff / t1_to_t2 if t1_to_t2 >= 1.0 else reference_teff
    binary = BinarySystem.from_json(system_dict)

    o = Observer(passband=passband, system=binary)
    o.observe.lc(phases=phases, normalize=True)
    return o.fluxes


def evaluate_prediction(predicted_parameters, true_parameters, reference_teff=None, passband=None, phases=None,
                        display_comparison=False, target_name=None, savepath=None):
    """
    This function evaluates quality of the predicted parameter set based on the cofficient of determination
    R^2 calculated between light curves constructed from predicted and true parameter sets.

    :param predicted_parameters: dict; predicted parameters set
    :param true_parameters: dict; true set of parameters
    :param reference_teff: reference temperature of the system, optional (set automatically)
    :param passband: str; name of the photometric filter used to evaluate curves
                          (see elisa.settings.PASSBANDS for all options)
    :param phases: numpy.ndarray; phases in which to evaluate the curve
    :param display_comparison; bool; if true, the comparison between the curves is displayed
    :param target_name: str; name of the target displayed in the plot
    :param savepath: str; place where to save the image
    :return: float; coefficient of determination R^2
    """
    passband = DEFAULT_PASSBAND if passband is None else passband
    phases = np.linspace(0.0, 1.0, 400, endpoint=False) if phases is None else None

    synthetic = evaluate_parameter_set(predicted_parameters, reference_teff, passband, phases)
    print("predicted params - eval function done")
    observed = evaluate_parameter_set(true_parameters, reference_teff, passband, phases)
    print('true params - eval function done')
    residual = np.sum([np.sum(np.power(synthetic[item] - observed[item], 2)) for item in observed])
    r2 = r_squared(synthetic, observed)
    print(f'R2 = {r2}')
    print(f'Residuals: {residual}')

    if display_comparison:
        fig = plt.figure(figsize=(8, 6))
        r2text = r'$R^2 = $' + str(round(r2, 2)) + r' Resid = ' + str(round(residual, 2))
        gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
        ax1 = fig.add_subplot(gs[0])
        ax2 = fig.add_subplot(gs[1], sharex=ax1)

        ax1.plot(phases, synthetic[passband], label='predicted')
        ax1.plot(phases, observed[passband], label='observed')

        ax2.plot(phases, synthetic[passband] - observed[passband])

        ax1.set_ylabel('Normalized flux')
        ax1.legend()
        ax2.set_xlabel('Phase')
        ax2.set_ylabel('Residuals')

        if target_name is not None:
            ax1.set_title(f'{target_name}, {r2text}')

        else:
            ax1.set_title(r2text)

        plt.subplots_adjust(hspace=0.0, top=0.95, right=0.97)

        if savepath:
            plt.savefig(f'{savepath}/' + str(target_name) + "diff_t")
        else:
            plt.show()

    return r2


if __name__ == "__main__":
    # Defined path to folder with true and predicted values
    target_csv = os.path.dirname(os.path.abspath(__file__)) + '\\data\\OBS_overcontact_model.csv'

    # Defined path to folder where we will save plotted light curves
    savepath = os.path.dirname(os.path.abspath(__file__)) + '\\data'

    df = pd.read_csv(target_csv)
    # df['name'] = "Orig pred - " + df['id'].astype(str) + "-" + df["filter"]  # for synthetic original
    # df['name'] = "Shift 1 up - " + df['id'].astype(str) + "-" + df["filter"]  # for synthetic shifited predictions
    # df['name'] = "Shift 2 up - " + df['id'].astype(str) + "-" + df["filter"]  # for synthetic shifited predictions
    # df['name'] = "Shift 1 down - " + df['id'].astype(str) + "-" + df["filter"]  # for synthetic shifited predictions
    # df['name'] = df['name'] + '-' + df['filter']  # for observed data
    # names = df['name'].unique() # use in case of using average values of parameters, e.g. for observed light curve we have more variations

    names = df['id']
    for name in names:
        print(f"Selected target: {name}")
        row = df[df['id'] == name]

        # Loading of PREDICTED values
        # need to check if name of columns are corresponding to the names of columns if csv file loaded
        predicted = dict(
            mass_ratio=float(row['p_q']),
            inclination=float(row['p_inc']),
            t1_to_t2=float(row['p_t1t2']),
            omega1=float(row['p_omega1']),
            omega2=float(row['p_omega2']),
            # r1=float(row['pred_prim_radius']),
            # r2=float(row['pred_sec_radius']),
        )

        # Loading of TRUE values
        # need to check if name of columns are corresponding to the names of columns if csv file loaded
        observed = dict(
            mass_ratio=float(row['mass_ratio']),
            inclination=float(row['inclination']),
            t1_to_t2=float(row['t1/t2']),
            omega1=float(row['primary__surface_potential']),
            omega2=float(row['secondary__surface_potential']),
            # r1=float(row['primary__equivalent_radius']),
            # r2=float(row['secondary__equivalent_radius']),
        )


        try:
            evaluate_prediction(predicted, observed, display_comparison=True, target_name=name, savepath=savepath)
        except Exception:
            print(traceback.format_exc())
            continue
