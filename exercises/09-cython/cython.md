
In this exercise,
you will create a Cython externsion `counting.pyx`
that provides the function `count_objects`.

1. Start with the following version of `counting.pyx`,

```python
# cython: profile=True
# cython linetrace=True

import numpy as np
cimport numpy as np

def count_objects(int[:, ::1] img):
    ny = img.shape[0]
    nx = img.shape[1]
    E = 0
    I = 0
    s = 0

    cdef Py_ssize_t i, j
    
    for i in range(ny-1):
        for j in range(nx-1):
            s = np.sum([img[i, j], img[i+1, j], img[i, j+1], img[i+1, j+1])
            if s == 1:
                E += 1
            elif s == 3:
                I += 1
    return (E - I)/4
```

2. You will also need to make a few additions to `setup.py` to
correctly build the extension:

```
from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

import numpy

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
```

To build the extension, you should do:

```shellsession
python setup.py build_ext -i
```

3. "Declare" the variables `nx`, `ny`, `E`, `I`, and `s`. The declarations
for loop variables `i` and `j` has already been done.

4. Replace the code that uses `np.sum` to compute the sum of the array values.

5. Make sure all your tests pass after making the above changes

6. Profile the code to see how much (if any) performance improvement
you get compared to the previous versions of `count_objects`.
