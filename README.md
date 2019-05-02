# PyICSF

Python implementation of the Intensity Conserving Spectral Fitting procedure
(ICSF) developed by [Klimchuk *et al.* (2016)][1].

[1]: http://adsabs.harvard.edu/abs/2016SoPh..291...55K

## Installation

Clone the repository (or download the sources), and install with pip:

~~~
git clone https://github.com/gpelouze/pyicsf
cd pyicsf
pip install .
~~~

## Usage

The ICSF procedure is implemented by the `pyicsf.icsf()` function, which takes
four arguments:

- `wvl` (1D array): wavelength positions.
- `I_obs` (1D array, same shape as `wvl`): observed intensities at the `wvl`
  positions.
- `min_err=1e-5` (float, optional): minimum error [F^i_avg − I_avg] at which
  the iteration stops.
- `max_iter=100` (int, optional): maximum number of iterations after which an
  exception is raised if the optimization has not converged.

This module also contains `pyicsf.bin_function()`, which integrates a function
within bins. It is used by `pyicsf.icsf()`, but can also generate synthetic
profiles from a known source function to test the procedure.


## Examples

**Very basic example:**

~~~python
import pyicsf
# generate a spectrum
wvl = np.linspace(-5.2, 4.8, 20)
I_obs = np.exp(-wvl**2)
# apply the ICSF procedure
I_corr = pyicsf.icsf(wvl, I_obs)
~~~

**More detailed example:** see [`example.py`](example.py), which was used to
generate the following plot:

![Plot showing the result of example.py](https://raw.githubusercontent.com/gpelouze/pyicsf/master/icsf_example.png)


## License

This package is released under a MIT open source licence. See
[`LICENSE.txt`](LICENSE.txt).
