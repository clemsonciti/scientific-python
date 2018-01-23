from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy as np

setup(name='micro',
    version='0.1',
    description='Tools for analysis of microscopic data',
    url='github.com/shwina/micro',
    author='Ashwin Srinath',
    license='MIT',
    packages=['micro'],
    ext_modules = cythonize([Extension("micro.counting",
                            ["micro/counting.pyx"],
                            include_dirs=[numpy.get_include()])]),
    zip_safe=False)
