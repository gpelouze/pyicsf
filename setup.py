import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='pyicsf',
    py_modules=['pyicsf'],
    version='2019.4.30',
    author='Gabriel Pelouze',
    author_email='gabriel.pelouze@ias.u-psud.fr',
    description='Python implementation of the Intensity Conserving Spectral Fitting (KlimchukEtAl2016)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gpelouze/pyicsf',
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    install_requires=['numpy>=1.15', 'scipy>=1.0'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
    ],
)
