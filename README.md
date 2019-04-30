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

See documentation of `pyicsf.icsf`.

Very basic example:

~~~python
import pyicsf
wvl = np.linspace(-5, 5, 20)
I_obs = np.exp(-wvl**2)
I_corr = pyicsf.icsf(wvl, I_obs)
plt.plot(wvl, I_obs)
plt.plot(wvl, I_corr)
~~~

More detailed example: see `example.py`.

![Plot showing the result of example.py][icsf_example.png]

## License

This package is released under a MIT open source licence. See `LICENSE.txt`.
