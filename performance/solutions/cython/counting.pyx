# cython: profile=True
# cython linetrace=True

import numpy as np
cimport numpy as np

def count_objects(int[:, ::1] img):
    cdef int ny = img.shape[0]
    cdef int nx = img.shape[1]
    cdef int E = 0
    cdef int I = 0
    cdef int s = 0
    cdef Py_ssize_t i, j
    
    for i in range(ny-1):
        for j in range(nx-1):
            s = img[i, j] + img[i+1, j] + img[i, j+1] + img[i+1, j+1]
            if s == 1:
                E += 1
            elif s == 3:
                I += 1
    return (E - I)/4
