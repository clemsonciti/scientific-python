
In this exercise,
you will create a Cython externsion `counting.pyx`
that provides the function `count_objects`.

1. Start with the following version of `counting.pyx`,
place the file in the same directory as `counting.py`:

```
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

2. "Declare" the variables `nx`, `ny`, `E`, `I`, and `s`. The declarations
for loop variables `i` and `j` has already been done.

3. Replace the code that uses `np.sum` to compute the sum of the array values.

4. Make sure all your tests pass after making the above changes

5. Profile the code to see how much (if any) performance improvement
you get compared to the previous versions of `count_objects`.
