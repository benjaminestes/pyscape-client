#!/usr/bin/env python

import os
import sys

from setuptools import setup

setup(
    name='pyscape-client',
    version='2015.02b2',
    description='Facilitate grabbing data from Moz API.',
    url='https://github.com/benjaminestes/pyscape',
    author='Benjamin Estes',
    author_email='benjamin.estes@distilled.net',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        # 'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='moz linkscape',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['pyscape'],

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['requests'],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #    'console_scripts': [
    #       'sample=sample:main',
    #    ],
    #},
)