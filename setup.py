#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name = 'noisi_v1',
    version = '0.0.0a0',
    description = 'Package to calculate noise correlations from precomputed\
 seismic wavefields',
    #long_description =
    # url = 
    author = 'L. Ermert, J. Igel, A. Fichtner',
    author_email  = 'laura.ermert@earth.ox.ac.uk, jigel@student.ethz.ch',
    # license
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Topic :: Seismology',
        'Programming Language :: Python :: 3',
    ],
    keywords = 'Ambient seismic noise',
    packages = find_packages(),
    #package_data = ,
    install_requires = [
        "obspy>=1.0.1",
        "geographiclib",
        "mpi4py>=2.0.0",
        "pandas",
        "instaseis",
        "h5py"],
    # ToDo: Use entry points in the future to handle two completely different approaches to the noise modeling: with delta-correlated sources or finite-correlation-length correlated sources
    # ToDo: Add entry points for test suite
    entry_points = {
        'console_scripts': [
            'noisi_v1 = noisi.main:run'            
        ]
    },
)

