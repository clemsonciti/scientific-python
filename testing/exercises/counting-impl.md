
In this exercise, you will implement
the function `count_objects` for which
you wrote tests in the previous
exercise.

The code for this function should be placed
in a file called `counting.py`
in the `micro` directory:

```shellsession
micro/
├── micro/
│   ├── counting.py
│   ├── __init__.py
├── README.md
├── LICENSE.md
├── setup.py
└── tests
    └── test_counting.py

```

The function implementation is given below,
but the code involves calls to two
helper functions `external_match`
and `internal_match`. Your task is to write the
code for these functions.

As a hint, you can use the `np.all` function
to check for the equality of two numpy
arrays:

```
# returns True if all elements of a are equal
# to the corresponding elements of b.
# returns False otherwise:
np.all(a == b) 
```

```python
import numpy as np


def count_objects(img):
    ny, nx = img.shape
    E = 0
    I = 0
    for i in range(nx-1):
        for j in range(ny-1):
            if external_match(img[i:i+2, j:j+2]):
                E += 1
            if internal_match(img[i:i+2, j:j+2]):
                I += 1
    return (E - I)/4

def external_match(a):
    """
    Checks if the given 2-by-2 array "a"
    is equal to any one of the following:

    a) 0 0  b) 0 0
       0 1     1 0

    c) 1 0  c) 0 1
       0 0     0 0

    If a match is found, then `True` is returned.
    Otherwise, `False` is returned.

    Parameters
    ----------

    a : array_like (size: [2, 2])
        A 2-by-2 binary array

    Returns
    -------

    True or False
    """
    # ------ YOUR CODE HERE ------ #



    # ---------------------------- #


def internal_match(a):
    """
    Checks if the given 2-by-2 array "a"
    is equal to any one of the following:

    a) 1 1  b) 1 1
       1 0     0 1

    c) 0 1  c) 1 0
       1 1     1 1

    If a match is found, then `True` is returned.
    Otherwise, `False` is returned.

    Parameters
    ----------

    a : array_like (size: [2, 2])
        A 2-by-2 binary array

    Returns
    -------

    True or False
    """
    # ------ YOUR CODE HERE ------ #



    # ---------------------------- #
```
