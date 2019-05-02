#!/usr/bin/env python3

import numpy as np
import scipy.interpolate as sinterp

def bin_function(f, bin_centers, points_in_bin=20):
    ''' Simulate the binning of a function at each given bin centers

    Parameters
    ==========
    f : callable
        Function to bin.
    bin_centers : array of shape (n,)
        Center of the bins.
        For a given bin center c_i, the bin edges are derived as:
            e_lower = (c_i + c_i-1) / 2
            e_upper = (c_i + c_i+1) / 2
        except for the first and last bin centers, for which the respective
        lower and upper bin edges are the bin center itself.
    points_in_bin : int (default: 20)
        Number of points used to integrate f within each bin

    Returns
    =======
    binned_data : array of shape (n,)
        Result of the binning. Each value corresponds to the integration of
        f within each bin.
    '''
    nbins = len(bin_centers)
    x_mid = (bin_centers[1:] + bin_centers[:-1]) / 2
    binned_data = np.zeros_like(bin_centers)
    for i in range(nbins):
        # integrate between x midpoints, except at the first and last bin
        # of the array where we integrate between x[0] and the next
        # midpoint, or between the last midpoint and x[-1]
        if i == 0:
            x_before = bin_centers[0]
            x_after = x_mid[0]
        elif i == nbins-1:
            x_before = x_mid[-1]
            x_after = bin_centers[-1]
        else:
            x_before = x_mid[i-1]
            x_after = x_mid[i]
        x_points = np.linspace(x_before, x_after, points_in_bin)
        y_points = f(x_points)
        new_ydata = np.sum(y_points) / points_in_bin
        binned_data[i] = new_ydata
    return binned_data

def icsf(wvl, I_obs, min_err=1e-5, max_iter=100):
    ''' Intensity conserving spectral fitting (Klimchuk+2016)

    Parameters
    ==========
    wvl : array of shape (n,)
        Wavelength positions
    I_obs : array of shape (n,)
        Observed intensities at the wvl positions
    min_err : float (default: 1e-5)
        Minimum error [F^i_avg - I_avg] at which the iteration stops.
    max_iter : int (default: 100)
        Maximum number of iterations after which the optimization fails if it
        has not converged.

    Raises
    ======
    RuntimeError :
        When the error is still larger than min_err after max_iter iterations
        have been performed.

    Returns
    =======
    I_corr : array of shape (n,)
        Intensities corrected through the ICSF method

    Example
    =======
    >>> I_corr = icsf(wvl, I_obs)
    '''
    # initialize iteration
    Fi_mid = I_obs
    # iter
    err = 2*min_err
    n_iter = 0
    while err > min_err:
        n_iter += 1
        if n_iter > max_iter:
            msg = 'Could not reach min_err in less than max_iter iterations'
            raise RuntimeError(msg)
        Fi = sinterp.make_interp_spline(wvl, Fi_mid)
        Fi_avg = bin_function(Fi, wvl)
        previous_Fi_mid = Fi_mid
        Fi_mid = I_obs * Fi_mid / Fi_avg
        err = np.mean(np.abs((Fi_avg - I_obs) / I_obs.max()))
    return Fi_mid
