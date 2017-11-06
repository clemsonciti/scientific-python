from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

setup(name='micro',
    version='0.1',
    description='Tools for analysis of microscopic data',
    url='github.com/shwina/micro',
    author='Ashwin Srinath',
    license='MIT',
    packages=['micro'],
    ext_modules = cythonize([Extension("micro.counting",
                            ["micro/counting.pyx"],
                            include_dirs=["/home/ashwin/software/miniconda/envs/scientific3/lib/python3.5/site-packages/numpy/core/include"])]),
    zip_safe=False)
