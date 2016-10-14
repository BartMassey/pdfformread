#!/usr/bin/python2
# Copyright (c) 2016 Bart Massey
# This code is available under the "MIT License".
# Please see the file COPYING in this distribution
# for license terms.

# PDF form miner / data extractor.

# http://python-packaging.readthedocs.io/en/latest/minimal.html

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pdfformread',
      version='0.1.2',
      description='Extract form data from a PDF form.',
      entry_points={
          'console_scripts': ['pdfformread=pdfformread.command_line:main'],
      },
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Office/Business',
      ],
      keywords='pdf form extract data',
      url='http://github.com/BartMassey/pdfformread',
      author='Bart Massey',
      author_email='bart.massey@gmail.com',
      license='MIT',
      packages=['pdfformread'],
      install_requires=['pdfminer'],
      include_package_data=True,
      zip_safe=False)
