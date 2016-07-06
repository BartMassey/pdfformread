#!/usr/bin/python2
# Copyright (c) 2016 Bart Massey
# This code is available under the "MIT License".
# Please see the file COPYING in this distribution
# for license terms.

# PDF form miner / data extractor.

# http://python-packaging.readthedocs.io/en/latest/minimal.html

from setuptools import setup

setup(name='pdfformparse',
      version='0.1',
      description='Extract form data from a PDF form.',
      url='http://github.com/BartMassey/pdfformread',
      author='Bart Massey',
      author_email='bart.massey@gmail.com',
      license='MIT',
      packages=['pdfformparse'],
      install_requires=['pdfminer'],
      zip_safe=False)
