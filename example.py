#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

import pyicsf

def f_spectrum(x, x0=195.12, s=30e-3, P=100):
    return P * np.exp( - (x - x0)**2 / (2 * s**2))

if __name__ == '__main__':
    plt.rcParams['axes.prop_cycle'] = plt.cycler('color', 
        ['#DDAA33', '#004488', '#BB5566', '#000000'])
    plt.rcParams['lines.linewidth'] = 1

    wvl_lim = (194.91, 195.4)
    wvl_fine = np.arange(*wvl_lim, 1e-3)
    wvl_coarse = np.arange(*wvl_lim, 22e-3)

    # high resolution spectrum:
    I_fine = f_spectrum(wvl_fine)
    # sampled spectrum (target result for ICSF):
    I_sampled = f_spectrum(wvl_coarse)
    # binned spectrum (what would be measured by a spectrometer):
    I_binned = pyicsf.bin_function(f_spectrum, wvl_coarse)

    # correct the observed spectrum with icsf
    I_icsf = pyicsf.icsf(wvl_coarse, I_binned)

    plt.clf()
    plt.plot(wvl_fine, I_fine, '-', linewidth=2, label='Input')
    plt.step(wvl_coarse, I_binned, '-', where='mid', label='Observed spectrum')
    plt.step(wvl_coarse, I_icsf, linestyle='--', where='mid', label='ICSF-corrected spectrum')
    plt.plot(wvl_coarse, I_sampled, '.', label='Sampled input (ICSF target)')
    plt.legend(frameon=False)
    plt.xlabel('Wavelength [Å]')
    plt.ylabel('Intensity')
    plt.savefig('icsf_example.png')
